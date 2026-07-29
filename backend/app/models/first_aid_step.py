from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy import SmallInteger
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base


class FirstAidStep(Base):
    __tablename__ = "first_aid_steps"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("emergency_categories.id"),
        nullable=False,
    )

    step_number: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False,
    )

    instruction_en: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    instruction_mm: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    category = relationship(
        "EmergencyCategory",
        back_populates="first_aid_steps",
    )