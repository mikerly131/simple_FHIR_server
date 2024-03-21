"""
The pydantic model for the slot resource based on FHIR R4 specification.

Slots are time-slots for a specific schedule, and don't provide appointment information.
Slots can have more than one appointment, but not in my system for now.
"""
from pydantic import BaseModel


class Slot(BaseModel):
    resource_type: str
    identifier: str
    service_category: str
    service_type: str
    specialty: str
    appointment_type: str
    schedule: str
    status: str
    start: str
    end: str
    overbooked: bool
    comment: str




