"""
The pydantic model for patient resource based on FHIR R4 specification.

Starting limited for my system.
"""
from resource import ResourceCreate, Resource
from human_name import HumanName
from contact_point import ContactPoint
from address import Address
from typing import Optional


class PatientCreate(ResourceCreate):
    active: bool
    name: list[HumanName]
    telecom: Optional[list[ContactPoint]] = None
    address: Optional[list[Address]] = None
    gender: Optional[str] = None
    birth_date: str
    deceased_boolean: bool
    multiple_birth: Optional[bool]


class Patient(PatientCreate, Resource):
    pass
