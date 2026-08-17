from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
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
            await MedicalFacilityRepository.get_nearby_facilities(
                db,
                latitude,
                longitude,
                limit,
            )
        )

        response = []

        for (
            facility,
            distance_meters,
            facility_latitude,
            facility_longitude,
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