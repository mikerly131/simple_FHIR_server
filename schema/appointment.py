"""
The pydantic model for appointment resource based on FHIR R4 specification.

Many attributes of appointments appear to be optional.
Using enums for attributes with limited value sets and required by spec or my system
"""
from pydantic import BaseModel
from schema.resource import ResourceCreate, Resource
from schema.codeable_concept import CodeableConcept
from typing import Optional
from enum import Enum


# Appointment status has defined set of possible values
class AppointmentStatus(str, Enum):
    proposed = 'proposed'
    pending = 'pending'
    booked = 'booked'
    arrived = 'arrived'
    fulfilled = 'fulfilled'
    cancelled = 'cancelled'
    noshow = 'noshow'
    error = 'entered-in-error'


# Appointment participants status has defined set of possible values
class ParticipantStatus(str, Enum):
    accepted = 'accepted'
    declined = 'declined'
    tentative = 'tentative'
    needs_actions = 'needs-action'


# Appointment participants are either required, optional or information-only
class ParticipantRequired(str, Enum):
    required = 'required'
    optional = 'optional'
    info_only = 'information-only'


# Appointments require one or more participants - patient, providers, and/or locations
class AppointmentParticipant(BaseModel):
    type: Optional[list[CodeableConcept]] = None
    actor: dict
    status: ParticipantStatus
    required: ParticipantRequired


class AppointmentCreate(ResourceCreate):
    status: AppointmentStatus
    cancelation_reason: Optional[CodeableConcept] = None
    service_category: Optional[list[CodeableConcept]] = None
    service_type: Optional[list[CodeableConcept]] = None
    specialty: Optional[list[CodeableConcept]] = None
    appointment_type: Optional[CodeableConcept] = None
    reason_code: Optional[CodeableConcept] = None
    reason_reference: Optional[list] = None
    priority: Optional[int] = None
    description: Optional[str] = None
    start: str
    end: str
    minutes_duration: Optional[int] = None
    slot: list[dict]
    comment: Optional[str] = None
    patient_instruction: Optional[str] = None
    participant: list[AppointmentParticipant]


class Appointment(AppointmentCreate, Resource):
    created: str
