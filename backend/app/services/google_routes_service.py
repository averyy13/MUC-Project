import re
import httpx
from fastapi import HTTPException, status
from app.core.config import settings

class GoogleRoutesService:
    ROUTES_URL = "https://routes.googleapis.com/directions/v2:computeRoutes"
    FIELD_MASK = "routes.distanceMeters,routes.duration,routes.polyline.encodedPolyline"

    @staticmethod
    async def compute_route(
        origin_latitude: float,
        origin_longitude: float,
        destination_latitude: float,
        destination_longitude: float,
    ) -> dict:
        payload = {
            "origin": {"location": {"latLng": {"latitude": origin_latitude, "longitude": origin_longitude}}},
            "destination": {"location": {"latLng": {"latitude": destination_latitude, "longitude": destination_longitude}}},
            "travelMode": "DRIVE",
            "routingPreference": "TRAFFIC_AWARE",
            "computeAlternativeRoutes": False,
            "routeModifiers": {"avoidTolls": False, "avoidHighways": False, "avoidFerries": False},
            "languageCode": "en-US",
            "units": "METRIC",
        }

        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": settings.GOOGLE_ROUTES_API_KEY,
            "X-Goog-FieldMask": GoogleRoutesService.FIELD_MASK,
        }

        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                response = await client.post(GoogleRoutesService.ROUTES_URL, json=payload, headers=headers)
        except httpx.RequestError as exc:
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, 
                detail=f"Unable to reach Google Routes API: {exc}") from exc
        print("GOOGLE ROUTES STATUS:", response.status_code)
        print("GOOGLE ROUTES RESPONSE:", response.text)
        if response.status_code != 200:
            try:
                error_body = response.json()
            except ValueError:
                error_body = response.text

            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail={"message": "Google Routes API returned an error", "google_status": response.status_code, "google_response": error_body},
            )

        try:
            data = response.json()
        except ValueError as exc:
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, 
                detail="Google Routes API returned invalid JSON") from exc

        routes = data.get("routes") or []
        if not routes:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                detail="Google Routes API could not find a route.")

        route = routes[0]
        distance_meters = route.get("distanceMeters")
        duration = route.get("duration")
        encoded_polyline = route.get("polyline", {}).get("encodedPolyline")

        if distance_meters is None or duration is None or not encoded_polyline:
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, 
                detail="Google Routes API response did not contain the expected route fields.")

        duration_seconds = GoogleRoutesService._parse_duration_seconds(duration)

        return {
            "distance_meters": int(distance_meters),
            "duration_seconds": duration_seconds,
            "encoded_polyline": encoded_polyline,
        }

    @staticmethod
    def _parse_duration_seconds(duration: str) -> int:
        match = re.fullmatch(r"([0-9]+(?:\.[0-9]+)?)s", duration)
        if not match:
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, 
                detail=f"Unexpected Google duration format: {duration}")
        return round(float(match.group(1)))