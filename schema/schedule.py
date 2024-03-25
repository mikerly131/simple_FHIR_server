"""
The pydantic model for the schedule resource based on FHIR R4 specification.

Schedule applies to a single actor, so may need to consult multiple to make appointment
Actors for my system - Patient, Provider, Location
May add HealthcareService and Device in future iterations
"""
from resource import ResourceCreate, Resource
from codeable_concept import CodeableConcept
from typing import Optional


class ScheduleCreate(ResourceCreate):
    active: bool
    service_category: Optional[list[CodeableConcept]] = None
    service_type: Optional[list[CodeableConcept]] = None
    specialty: Optional[list[CodeableConcept]] = None
    actor: list[dict[str, str]]
    planning_horizon: Optional[list[dict[str, str]]] = None
    comment: Optional[str]


class Schedule(ScheduleCreate, Resource):
    pass
