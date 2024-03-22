"""
The pydantic model for patient resource based on FHIR R4 specification.

Starting limited for my system.
"""
from resource import ResourceCreate, Resource
from typing import Optional
from enum import Enum


class PatientCreate(ResourceCreate):
    active: bool
    name: list[dict]
    telecom: Optional[list[dict]] = None
    address: Optional[list[dict]] = None
    gender: Optional[str] = None
    birth_date: str
    deceased_boolean: bool
    multiple_birth: Optional[bool]


class Patient(PatientCreate, Resource):
    pass
