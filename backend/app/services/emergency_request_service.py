from geoalchemy2.elements import WKTElement
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.emergency_request import EmergencyRequest
from app.repositories.emergency_request_repository import EmergencyRequestRepository
from app.repositories.spatial_repository import SpatialRepository


class EmergencyService:

    @staticmethod
    async def create_sos(db: AsyncSession, data):
        # Convert lat/lon into WKT point (Longitude comes FIRST in PostGIS ST_Point)
        point_wkt = WKTElement(f"POINT({data.longitude} {data.latitude})", srid=4326)

        emergency = EmergencyRequest(
            category_id=data.category_id,
            location=point_wkt,
        )

        await EmergencyRequestRepository.create(db, emergency)

        volunteers = await SpatialRepository.nearest_volunteers(
            db, data.latitude, data.longitude, limit=20
        )
        rescue = await SpatialRepository.nearest_rescue_contacts(
            db, data.latitude, data.longitude, limit=3
        )
        facilities = await SpatialRepository.nearest_facilities(
            db, data.latitude, data.longitude, limit=5
        )

        await db.commit()

        return {
            "emergency_id": emergency.id,
            "matched_volunteers": volunteers,
            "rescue_contacts": rescue,
            "medical_facilities": facilities,
        }