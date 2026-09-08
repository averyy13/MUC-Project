from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, cast, Float
from sqlalchemy.orm import selectinload
from geoalchemy2 import Geometry
from geoalchemy2.functions import ST_Y, ST_X

from app.models.enums import ApprovalStatus, EmergencyStatus
from app.models.emergency_request import EmergencyRequest
from app.models.volunteer import Volunteer
from app.models.medical_facility import MedicalFacility
from app.models.emergency_contact import EmergencyContact
from app.repositories.admin_repository import AdminRepository

class AdminService:
    # ── Existing volunteer management ──────────────────────────

    @staticmethod
    async def list_pending(db: AsyncSession):
        volunteers = await AdminRepository.get_volunteers_by_status(
            db,
            ApprovalStatus.PENDING,
        )
        return [
            {
                "volunteer_id": str(v.id),
                "full_name": v.user.full_name,
                "phone": v.user.phone,
                "email": v.user.email,
                "nrc_number": v.nrc_number,
                "address": v.address,
                "approval_status": v.approval_status.value,
                "created_at": v.created_at.isoformat() if v.created_at else None,
                "completed_rescues": count,
                "current_location": {"lat": lat, "lng": lng} if lat is not None and lng is not None else None,
            }
            for v, count, lng, lat in volunteers
        ]

    @staticmethod
    async def list_approved(db: AsyncSession):
        volunteers = await AdminRepository.get_volunteers_by_status(
            db,
            ApprovalStatus.APPROVED,
        )
        return [
            {
                "volunteer_id": str(v.id),
                "full_name": v.user.full_name,
                "phone": v.user.phone,
                "email": v.user.email,
                "nrc_number": v.nrc_number,
                "address": v.address,
                "availability": v.availability,
                "approval_status": v.approval_status.value,
                "created_at": v.created_at.isoformat() if v.created_at else None,
                "completed_rescues": count,
                "current_location": {"lat": lat, "lng": lng} if lat is not None and lng is not None else None,
            }
            for v, count, lng, lat in volunteers
        ]

    @staticmethod
    async def list_rejected(db: AsyncSession):
        volunteers = await AdminRepository.get_volunteers_by_status(
            db,
            ApprovalStatus.REJECTED,
        )
        return [
            {
                "volunteer_id": str(v.id),
                "full_name": v.user.full_name,
                "phone": v.user.phone,
                "email": v.user.email,
                "nrc_number": v.nrc_number,
                "address": v.address,
                "approval_status": v.approval_status.value,
                "created_at": v.created_at.isoformat() if v.created_at else None,
                "completed_rescues": count,
                "current_location": {"lat": lat, "lng": lng} if lat is not None and lng is not None else None,
            }
            for v, count, lng, lat in volunteers
        ]

    @staticmethod
    async def approve(db: AsyncSession, volunteer_id):
        volunteer = await AdminRepository.get_volunteer(db, volunteer_id)

        if volunteer is None:
            raise HTTPException(404, "Volunteer not found")

        await AdminRepository.update_status(
            db,
            volunteer,
            ApprovalStatus.APPROVED,
        )

        await db.commit()

        return {
            "volunteer_id": str(volunteer.id),
            "full_name": volunteer.user.full_name,
            "phone": volunteer.user.phone,
            "approval_status": volunteer.approval_status.value,
        }

    @staticmethod
    async def reject(db: AsyncSession, volunteer_id):
        volunteer = await AdminRepository.get_volunteer(db, volunteer_id)

        if volunteer is None:
            raise HTTPException(404, "Volunteer not found")

        await AdminRepository.update_status(
            db,
            volunteer,
            ApprovalStatus.REJECTED,
        )

        await db.commit()

        return {
            "volunteer_id": str(volunteer.id),
            "full_name": volunteer.user.full_name,
            "phone": volunteer.user.phone,
            "approval_status": volunteer.approval_status.value,
        }

    # ── New admin dashboard endpoints ──────────────────────────

    @staticmethod
    async def get_dashboard_stats(db: AsyncSession):
        # Emergency counts by status
        emergency_counts_q = (
            select(
                EmergencyRequest.status,
                func.count().label("cnt"),
            )
            .group_by(EmergencyRequest.status)
        )
        result = await db.execute(emergency_counts_q)
        status_counts = {row.status: row.cnt for row in result}

        searching = status_counts.get(EmergencyStatus.SEARCHING, 0)
        assigned = status_counts.get(EmergencyStatus.ASSIGNED, 0)
        en_route = status_counts.get(EmergencyStatus.VOLUNTEER_EN_ROUTE, 0)
        completed = status_counts.get(EmergencyStatus.COMPLETED, 0)
        active = searching + assigned + en_route

        # Pending volunteers
        pending_q = select(func.count()).select_from(Volunteer).where(
            Volunteer.approval_status == ApprovalStatus.PENDING
        )
        pending_result = await db.execute(pending_q)
        pending_volunteers = pending_result.scalar() or 0

        # Available volunteers (approved AND online)
        available_q = select(func.count()).select_from(Volunteer).where(
            Volunteer.approval_status == ApprovalStatus.APPROVED,
            Volunteer.availability == True,
        )
        available_result = await db.execute(available_q)
        available_volunteers = available_result.scalar() or 0

        # Facilities count
        facilities_q = select(func.count()).select_from(MedicalFacility)
        facilities_result = await db.execute(facilities_q)
        total_facilities = facilities_result.scalar() or 0

        # Rescue organizations count
        contacts_q = select(func.count()).select_from(EmergencyContact)
        contacts_result = await db.execute(contacts_q)
        total_rescue_organizations = contacts_result.scalar() or 0

        return {
            "active_emergencies": active,
            "searching_emergencies": searching,
            "en_route_emergencies": en_route,
            "pending_volunteers": pending_volunteers,
            "available_volunteers": available_volunteers,
            "completed_rescues": completed,
            "total_facilities": total_facilities,
            "total_rescue_organizations": total_rescue_organizations,
        }

    @staticmethod
    async def get_emergencies_over_time(db: AsyncSession, period: str):
        from datetime import datetime, timedelta, timezone
        now = datetime.now(timezone.utc)
        
        if period == "30d":
            start_date = now - timedelta(days=29)
        elif period == "3m":
            start_date = now - timedelta(days=89)
        else:
            start_date = now - timedelta(days=6) # 7 days including today
        
        from sqlalchemy import select, func
        from app.models.emergency_request import EmergencyRequest
        
        # We need to extract the date from created_at
        # Assuming postgresql timezone mapping, but func.date() works in SQLAlchemy for postgres.
        # However, to avoid time zone issues and make it robust, we can cast to date.
        query = (
            select(
                func.date(EmergencyRequest.created_at).label('day'),
                func.count(EmergencyRequest.id).label('count')
            )
            .where(EmergencyRequest.created_at >= start_date.replace(hour=0, minute=0, second=0, microsecond=0))
            .group_by(func.date(EmergencyRequest.created_at))
            .order_by(func.date(EmergencyRequest.created_at))
        )
        result = await db.execute(query)
        rows = result.all()
        
        data = {}
        for row in rows:
            if row.day:
                data[row.day.strftime('%Y-%m-%d')] = row.count
            
        days = (now.date() - start_date.date()).days
        result_list = []
        
        for i in range(days + 1):
            d = (start_date + timedelta(days=i)).date()
            ds = d.strftime('%Y-%m-%d')
            result_list.append({
                "date": ds,
                "label": d.strftime('%b %d'),
                "count": data.get(ds, 0)
            })
            
        return result_list

    @staticmethod
    async def get_emergencies_by_category(db: AsyncSession):
        from sqlalchemy import select, func
        from app.models.emergency_request import EmergencyRequest
        from app.models.emergency_category import EmergencyCategory
        
        query = (
            select(
                EmergencyCategory.name_en,
                func.count(EmergencyRequest.id).label('count')
            )
            .outerjoin(EmergencyRequest, EmergencyRequest.category_id == EmergencyCategory.id)
            .group_by(EmergencyCategory.id, EmergencyCategory.name_en)
            .order_by(func.count(EmergencyRequest.id).desc())
        )
        result = await db.execute(query)
        rows = result.all()
        
        return [
            {
                "category": row.name_en,
                "count": row.count
            }
            for row in rows
        ]

    @staticmethod
    async def list_emergencies(db: AsyncSession, status_filter: str | None = None):
        # Cast Geography → Geometry before extracting coordinates
        location_geom = cast(EmergencyRequest.location, Geometry("POINT", srid=4326))
        query = (
            select(
                EmergencyRequest,
                func.ST_Y(location_geom).label("latitude"),
                func.ST_X(location_geom).label("longitude"),
            )
            .options(
                selectinload(EmergencyRequest.category),
                selectinload(EmergencyRequest.assigned_volunteer).selectinload(Volunteer.user),
            )
            .order_by(EmergencyRequest.created_at.desc())
        )

        if status_filter:
            try:
                status_enum = EmergencyStatus(status_filter)
                query = query.where(EmergencyRequest.status == status_enum)
            except ValueError:
                pass  # Ignore invalid status filter

        result = await db.execute(query)
        rows = result.all()

        emergencies = []
        for emergency, lat, lng in rows:
            vol_name = None
            vol_phone = None
            if emergency.assigned_volunteer and emergency.assigned_volunteer.user:
                vol_name = emergency.assigned_volunteer.user.full_name
                vol_phone = emergency.assigned_volunteer.user.phone

            emergencies.append({
                "emergency_id": str(emergency.id),
                "status": emergency.status.value,
                "category_id": emergency.category_id,
                "category_name_en": emergency.category.name_en if emergency.category else "",
                "category_name_mm": emergency.category.name_mm if emergency.category else "",
                "description": emergency.description,
                "latitude": float(lat) if lat is not None else 0.0,
                "longitude": float(lng) if lng is not None else 0.0,
                "created_at": emergency.created_at.isoformat() if emergency.created_at else None,
                "updated_at": emergency.updated_at.isoformat() if emergency.updated_at else None,
                "assigned_volunteer_name": vol_name,
                "assigned_volunteer_phone": vol_phone,
            })

        return emergencies

    @staticmethod
    async def list_facilities(db: AsyncSession):
        # Cast Geography → Geometry before extracting coordinates
        location_geom = cast(MedicalFacility.location, Geometry("POINT", srid=4326))
        query = select(
            MedicalFacility,
            func.ST_Y(location_geom).label("latitude"),
            func.ST_X(location_geom).label("longitude"),
        )
        result = await db.execute(query)
        rows = result.all()

        return [
            {
                "id": str(facility.id),
                "name_en": facility.name_en,
                "name_mm": facility.name_mm,
                "phone": facility.phone,
                "address_en": facility.address_en,
                "address_mm": facility.address_mm,
                "type": facility.type.value,
                "latitude": float(lat) if lat is not None else 0.0,
                "longitude": float(lng) if lng is not None else 0.0,
                "is_active": facility.is_active,
            }
            for facility, lat, lng in rows
        ]

    @staticmethod
    async def list_emergency_contacts(db: AsyncSession):
        # Cast Geography → Geometry before extracting coordinates
        location_geom = cast(EmergencyContact.location, Geometry("POINT", srid=4326))
        query = select(
            EmergencyContact,
            func.ST_Y(location_geom).label("latitude"),
            func.ST_X(location_geom).label("longitude"),
        )
        result = await db.execute(query)
        rows = result.all()

        return [
            {
                "id": str(contact.id),
                "name_en": contact.name_en,
                "name_mm": contact.name_mm,
                "phone": contact.phone,
                "type": contact.type.value,
                "latitude": float(lat) if lat is not None else 0.0,
                "longitude": float(lng) if lng is not None else 0.0,
                "is_active": contact.is_active,
            }
            for contact, lat, lng in rows
        ]

    from app.schemas.admin import MedicalFacilityUpdate, EmergencyContactUpdate
    from app.models.enums import MedicalFacilityType, OrganizationType

    @staticmethod
    async def update_facility(db: AsyncSession, facility_id, update_data):
        from app.models.enums import MedicalFacilityType
        query = select(MedicalFacility).where(MedicalFacility.id == facility_id)
        result = await db.execute(query)
        facility = result.scalar_one_or_none()
        
        if not facility:
            raise HTTPException(status_code=404, detail="Medical facility not found")

        update_dict = update_data.model_dump(exclude_unset=True)
        if "type" in update_dict and update_dict["type"] is not None:
            try:
                update_dict["type"] = MedicalFacilityType(update_dict["type"])
            except ValueError:
                raise HTTPException(status_code=422, detail="Invalid facility type")

        if "latitude" in update_dict and "longitude" in update_dict:
            lat = update_dict.pop("latitude")
            lng = update_dict.pop("longitude")
            if lat is not None and lng is not None:
                if not (-90 <= lat <= 90) or not (-180 <= lng <= 180):
                    raise HTTPException(status_code=422, detail="Invalid coordinates")
                facility.location = f"SRID=4326;POINT({lng} {lat})"

        for key, value in update_dict.items():
            setattr(facility, key, value)
            
        await db.commit()
        await db.refresh(facility)
        return {"status": "success", "id": facility.id}

    @staticmethod
    async def deactivate_facility(db: AsyncSession, facility_id):
        query = select(MedicalFacility).where(MedicalFacility.id == facility_id)
        result = await db.execute(query)
        facility = result.scalar_one_or_none()
        
        if not facility:
            raise HTTPException(status_code=404, detail="Medical facility not found")
            
        facility.is_active = False
        await db.commit()
        return {"status": "success", "id": facility.id}

    @staticmethod
    async def update_emergency_contact(db: AsyncSession, contact_id, update_data):
        from app.models.enums import OrganizationType
        query = select(EmergencyContact).where(EmergencyContact.id == contact_id)
        result = await db.execute(query)
        contact = result.scalar_one_or_none()
        
        if not contact:
            raise HTTPException(status_code=404, detail="Emergency contact not found")

        update_dict = update_data.model_dump(exclude_unset=True)
        if "type" in update_dict and update_dict["type"] is not None:
            try:
                update_dict["type"] = OrganizationType(update_dict["type"])
            except ValueError:
                raise HTTPException(status_code=422, detail="Invalid organization type")

        if "latitude" in update_dict and "longitude" in update_dict:
            lat = update_dict.pop("latitude")
            lng = update_dict.pop("longitude")
            if lat is not None and lng is not None:
                if not (-90 <= lat <= 90) or not (-180 <= lng <= 180):
                    raise HTTPException(status_code=422, detail="Invalid coordinates")
                contact.location = f"SRID=4326;POINT({lng} {lat})"

        for key, value in update_dict.items():
            setattr(contact, key, value)
            
        await db.commit()
        await db.refresh(contact)
        return {"status": "success", "id": contact.id}

    @staticmethod
    async def deactivate_emergency_contact(db: AsyncSession, contact_id):
        query = select(EmergencyContact).where(EmergencyContact.id == contact_id)
        result = await db.execute(query)
        contact = result.scalar_one_or_none()
        
        if not contact:
            raise HTTPException(status_code=404, detail="Emergency contact not found")
            
        contact.is_active = False
        await db.commit()
        return {"status": "success", "id": contact.id}