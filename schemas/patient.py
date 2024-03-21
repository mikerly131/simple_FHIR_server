"""
The pydantic model for patient resource based on FHIR R4 specification.
"""
from pydantic import BaseModel


class Patient(BaseModel):
    resource_type: str
    id: str