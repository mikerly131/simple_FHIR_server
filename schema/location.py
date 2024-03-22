"""
The pydantic model for location resource based on FHIR R4 specification.

Locations will have schedules with slots, and be used for appointments.
Keeping it light in my system: buildings and rooms in buildings
"""
from resource import ResourceCreate, Resource
from typing import Optional
from enum import Enum


class LocationStatus(str, Enum):
    active = 'active'
    suspended = 'suspended'
    inactive = 'inactive'


class LocationCreate(ResourceCreate):
    status: LocationStatus
    name: str
    alias: Optional[list[str]] = None
    description: str
    type: Optional[list] = None
    physical_type: Optional[dict] = None
    telecom: Optional[list[dict]] = None
    address: Optional[dict] = None
    partOf: Optional[dict] = None


class Location(LocationCreate, Resource):
    pass
