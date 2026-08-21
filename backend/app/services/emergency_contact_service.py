from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.emergency_contact_repository import (
    EmergencyContactRepository,
)
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

        for (
            contact,
            distance_meters,
            contact_latitude,
            contact_longitude,
        ) in contacts:

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