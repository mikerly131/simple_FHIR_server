"""
The pydantic model for location resource based on FHIR R4 specification.

Locations will have schedules with slots, and be used for appointments.
"""
from pydantic import BaseModel


class Location(BaseModel):
    resource_type: str
    id: str
