"""
The pydantic model for the slot resource based on FHIR R4 specification.

Slots are time-slots for a specific schedule, and don't have to provide appointment information.
Slots can have more than one appointment, but not in my system for now.
serviceCategory, serviceType, speciality, appointmentType:
- what slot can be used for, not appointment details in my system
"""
from pydantic import BaseModel
from typing import Optional
from enum import Enum


# Slots have a mandatory status
class SlotStatus(str, Enum):
    busy = 'busy'
    free = 'free'
    unavailable = 'busy-unavailable'
    tentative = 'busy-tentative'
    error = 'entered-in-error'


class Slot(BaseModel):
    resource_type: str
    id: str
    text: Optional[dict] = None
    identifier: Optional[list] = None
    service_category: Optional[list] = None
    service_type: Optional[list] = None
    specialty: Optional[list] = None
    appointment_type: Optional[list] = None
    schedule: dict
    status: SlotStatus
    start: str
    end: str
    overbooked: bool
    comment: Optional[str] = None




