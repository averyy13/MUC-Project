import uuid
from datetime import datetime

from geoalchemy2 import Geography
from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import ApprovalStatus
from sqlalchemy.orm import relationship


class Volunteer(Base):
    __tablename__ = "volunteers"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    nrc_number: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    address: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    home_location = mapped_column(
        Geography("POINT", srid=4326),
        nullable=True,
    )

    certificate_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    approval_status: Mapped[ApprovalStatus] = mapped_column(
        Enum(ApprovalStatus, name="approval_status"),
        default=ApprovalStatus.PENDING,
    )

    availability: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
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

    user = relationship(
        "User",
        back_populates="volunteer",
    )
    current_location = relationship(
        "CurrentVolunteerLocation",
        back_populates="volunteer",
        uselist=False,
        cascade="all, delete-orphan"
    )
    device_tokens = relationship(
        "DeviceToken",
        back_populates="volunteer",
        cascade="all, delete-orphan",
    )
    notifications = relationship(
        "EmergencyNotification",
        back_populates="volunteer",
        cascade="all, delete-orphan",
    )