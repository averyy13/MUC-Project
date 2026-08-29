from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.emergency_contact_repository import (
    EmergencyContactRepository,
)
from uuid import UUID
from app.services.google_routes_service import GoogleRoutesService
class EmergencyContactService:
    @staticmethod
    async def get_nearby_rescue_teams(
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
        contacts = (
            await EmergencyContactRepository
            .get_nearby_rescue_teams(
                db=db,
                latitude=latitude,
                longitude=longitude,
                limit=limit,
            )
        )
        response = []

        for ( contact,distance_meters,contact_latitude,contact_longitude,) in contacts:
            response.append(
                {
                    "id": str(contact.id),
                    "name_en": contact.name_en,
                    "name_mm": contact.name_mm,
                    "phone": contact.phone,
                    "type": contact.type.value,
                    "latitude": float(contact_latitude),
                    "longitude": float(contact_longitude),
                    "distance_km": round(
                        float(distance_meters) / 1000,
                        2,
                    ),
                }
            )
        return response
    
    @staticmethod
    async def get_route_to_contact(
        db: AsyncSession,
        contact_id: UUID,
        user_latitude: float,
        user_longitude: float,
    ):
        result = await EmergencyContactRepository.get_by_id_with_coordinates(
            db,
            contact_id,
        )
    
        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Emergency contact not found.",
            )
    
        contact, contact_latitude, contact_longitude = result
    
        route = await GoogleRoutesService.compute_route(
            origin_latitude=user_latitude,
            origin_longitude=user_longitude,
            destination_latitude=float(contact_latitude),
            destination_longitude=float(contact_longitude),
        )
    
        return {
            "contact_id": contact.id,
            "user_latitude": user_latitude,
            "user_longitude": user_longitude,
            "contact_latitude": float(contact_latitude),
            "contact_longitude": float(contact_longitude),
            "distance_meters": route["distance_meters"],
            "duration_seconds": route["duration_seconds"],
            "encoded_polyline": route["encoded_polyline"],
        }