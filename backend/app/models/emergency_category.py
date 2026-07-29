from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class EmergencyCategory(Base):
    __tablename__ = "emergency_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name_en: Mapped[str] = mapped_column(String(100), nullable=False)

    name_mm: Mapped[str] = mapped_column(String(100), nullable=False)

    priority: Mapped[int] = mapped_column(Integer, nullable=False)
    
    emergency_requests = relationship(
        "EmergencyRequest",
        back_populates="category",
    )
    first_aid_steps = relationship(
        "FirstAidStep",
        back_populates="category",
        cascade="all, delete-orphan",
    )