"""
The pydantic model for the slot resource based on FHIR R4 specification.

Slots are time-slots for a specific schedule, and don't have to provide appointment information.
Slots can have more than one appointment, but not in my system for now.
serviceCategory, serviceType, speciality, appointmentType:
- what slot can be used for, not appointment details in my system
"""
from resource import ResourceCreate, Resource
from typing import Optional
from enum import Enum


# Slots have a mandatory status
class SlotStatus(str, Enum):
    busy = 'busy'
    free = 'free'
    unavailable = 'busy-unavailable'
    tentative = 'busy-tentative'
    error = 'entered-in-error'


class SlotCreate(ResourceCreate):
    service_category: Optional[list] = None
    service_type: Optional[list] = None
    specialty: Optional[list] = None
    appointment_type: Optional[list] = None
    schedule: dict[str, str]
    status: SlotStatus
    start: str
    end: str
    overbooked: bool
    comment: Optional[str] = None


class Slot(SlotCreate, Resource):
    pass


