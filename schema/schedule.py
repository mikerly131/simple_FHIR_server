"""
The pydantic model for the schedule resource based on FHIR R4 specification.

Schedule applies to a single actor, so may need to consult multiple to make appointment
Actors for my system - Patient, Provider, Location
May add HealthcareService and Device in future iterations
"""
from resource import ResourceCreate, Resource


class ScheduleCreate(ResourceCreate):
    active: bool
    actor: list[dict[str, str]]
    planning_horizon: list[dict[str, str]]
    comment: str


class Schedule(ScheduleCreate, Resource):
    pass
