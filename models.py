from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String)
    specialization: Mapped[str] = mapped_column(String)
    phone_number: Mapped[str] = mapped_column(String)

    patients: Mapped[list["Patient"]] = relationship(back_populates="doctor")


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String)
    birth_date: Mapped[str] = mapped_column(String)
    phone_number: Mapped[str] = mapped_column(String)
    doctor_id: Mapped[int | None] = mapped_column(ForeignKey("doctors.id"),nullable=True)
    image: Mapped[str | None] = mapped_column(String, default=None)
    video: Mapped[str | None] = mapped_column(String, default=None)

    doctor: Mapped["Doctor"] = relationship(back_populates="patients")