"""
DB Model for Patient resource
"""
from models.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import ForeignKey, String
from typing import Optional


class Slot(Base):
    __tablename__ = 'patient'

    resource_id: Mapped[str] = mapped_column(primary_key=True)
    resource_data: Mapped[list] = mapped_column(JSON)
