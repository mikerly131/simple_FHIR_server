"""
The pydantic model for provider resource based on FHIR R4 specification.
"""
from pydantic import BaseModel


class Provider(BaseModel):
    resource_type: str
    id: str