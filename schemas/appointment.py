"""
The pydantic model for appointment resource based on FHIR R4 specification.

I'm choosing to implement a lot of the elements for learning purposes, examples show less are often used.
"""
from pydantic import BaseModel
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


# Appointments require one or more participants - patient, providers, and/or locations
class AppointmentParticipant(BaseModel):
    type: str
    actor: str
    status: ParticipantStatus


class Appointment(BaseModel):
    resource_type: str
    id: str
    identifier: list
    status: AppointmentStatus
    cancelation_reason: str | None = None
    service_category: str
    service_type: str
    speciality: str
    appointment_type: str
    reason_code: str
    reason_reference: str
    priority: str
    description: str
    start: str
    end: str
    minutes_duration: int
    slot: str
    created: str
    comment: str
    patient_instruction: str
    participant: AppointmentParticipant
