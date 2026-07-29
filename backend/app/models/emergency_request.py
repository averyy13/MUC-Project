from __future__ import annotations
from sqlalchemy import Enum as SQLEnum
from app.models.enums import EmergencyStatus
import uuid
from datetime import datetime
from geoalchemy2 import Geography
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base


class EmergencyRequest(Base):
    __tablename__ = "emergency_requests"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("emergency_categories.id"),
        nullable=False,
    )

    requester_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    location: Mapped[object] = mapped_column(
        Geography(geometry_type="POINT", srid=4326),
        nullable=False,
    )

    status: Mapped[EmergencyStatus] = mapped_column(
        SQLEnum(
            EmergencyStatus,
            name="emergency_status",
            create_type=False,
        ),
        nullable=False,
        default=EmergencyStatus.SEARCHING,
        server_default="SEARCHING",
    )

    assigned_volunteer_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("volunteers.id"),
        nullable=True,
    )

    assigned_rescue_contact_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("emergency_contacts.id"),
        nullable=True,
    )

    accepted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Relationships

    category = relationship(
        "EmergencyCategory",
        back_populates="emergency_requests",
    )

    requester = relationship(
        "User",
        back_populates="emergency_requests",
    )

    assigned_volunteer = relationship(
        "Volunteer",
        foreign_keys=[assigned_volunteer_id],
    )

    assigned_rescue_contact = relationship(
        "EmergencyContact",
        foreign_keys=[assigned_rescue_contact_id],
    )
    
    notifications = relationship(
        "EmergencyNotification",
        back_populates="emergency_request",
        cascade="all, delete-orphan",
    )