"""
The pydantic model for provider resource based on FHIR R4 specification.

Keeping data limited for my system
"""
from resource import ResourceCreate, Resource
from address import Address
from contact_point import ContactPoint
from typing import Optional


class PractitionerCreate(ResourceCreate):
    active: bool
    name: list[dict]
    telecom: Optional[list[ContactPoint]] = None
    address: Optional[list[Address]] = None
    gender: Optional[str] = None
    birth_date: str


class Practitioner(PractitionerCreate, Resource):
    pass
