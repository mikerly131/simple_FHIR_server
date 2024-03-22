"""
The pydantic model for provider resource based on FHIR R4 specification.

Keeping data limited for my system
"""
from resource import ResourceCreate, Resource
from typing import Optional


class PractitionerCreate(ResourceCreate):
    active: bool
    name: list[dict]
    telecom: Optional[list[dict]] = None
    address: Optional[list[dict]] = None
    gender: Optional[str] = None
    birth_date: str


class Practitioner(PractitionerCreate, Resource):
    pass
