"""
DB Model for Practitioner resource
"""
from models.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import ForeignKey, String
from typing import Optional


class Practitioner(Base):
    __tablename__ = 'practitioner'

    resource_id: Mapped[str] = mapped_column(primary_key=True)
    resource_data: Mapped[list] = mapped_column(JSON)

