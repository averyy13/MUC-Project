import uuid
from datetime import datetime

from geoalchemy2 import Geography
from sqlalchemy import DateTime, Float, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class CurrentVolunteerLocation(Base):

    __tablename__ = "current_volunteer_locations"

    volunteer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "volunteers.id",
            ondelete="CASCADE"
        ),
        primary_key=True
    )

    location = mapped_column(
        Geography(
            geometry_type="POINT",
            srid=4326
        ),
        nullable=False
    )

    speed: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    heading: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )


    volunteer = relationship(
        "Volunteer",
        back_populates="current_location"
    )