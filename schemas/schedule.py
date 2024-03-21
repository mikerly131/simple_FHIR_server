"""
The pydantic model for the schedule resource based on FHIR R4 specification.

I'm choosing to implement a lot of the elements for learning purposes, examples show less are often used.
"""
from pydantic import BaseModel


class Schedule(BaseModel):
    resource_type: str
    id: str
    identifier: str
    active: bool
    service_category: str
    service_type: str
    speciality: str
    actor: str
    planning_horizon: str
    comment: str