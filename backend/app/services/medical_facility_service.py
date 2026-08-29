from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.services.google_routes_service import GoogleRoutesService
from app.repositories.medical_facility_repository import (
    MedicalFacilityRepository,
)
class MedicalFacilityService:
    @staticmethod
    async def get_nearby_facilities(
        db: AsyncSession,
        latitude: float,
        longitude: float,
        limit: int = 5,
    ):
        if limit < 1 or limit > 20:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Limit must be between 1 and 20",
            )
        facilities = (
            await MedicalFacilityRepository.get_nearby_facilities( db,latitude,longitude,limit,)
        )
        response = []
        for (facility,distance_meters,facility_latitude,facility_longitude,
        ) in facilities:
            response.append({
                "id": facility.id,
                "name_en": facility.name_en,
                "name_mm": facility.name_mm,
                "phone": facility.phone,
                "address_en": facility.address_en,
                "address_mm": facility.address_mm,
                "type": facility.type.value,
                "latitude": float(facility_latitude),
                "longitude": float(facility_longitude),
                "distance_km": round(
                    float(distance_meters) / 1000,
                    2,
                ),
            })
        return response
    
    @staticmethod
    async def get_route_to_facility(
        db: AsyncSession,
        facility_id: UUID,
        user_latitude: float,
        user_longitude: float,
    ):
        result = await MedicalFacilityRepository.get_by_id_with_coordinates(
            db,
            facility_id,
        )

        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medical facility not found.",
            )

        facility, facility_latitude, facility_longitude = result

        route = await GoogleRoutesService.compute_route(
            origin_latitude=user_latitude,
            origin_longitude=user_longitude,
            destination_latitude=float(facility_latitude),
            destination_longitude=float(facility_longitude),
        )

        return {
            "facility_id": facility.id,

            "user_latitude": user_latitude,
            "user_longitude": user_longitude,

            "facility_latitude": float(facility_latitude),
            "facility_longitude": float(facility_longitude),

            "distance_meters": route["distance_meters"],
            "duration_seconds": route["duration_seconds"],
            "encoded_polyline": route["encoded_polyline"],
        }