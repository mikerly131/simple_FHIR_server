"""
The base model for resources - data common to any resource in FHIR R4 spec

identifier is not an attribute of DomainResource in FHIR R4, but common to all resources my system uses
"""
from pydantic import BaseModel
from typing import Optional


class ResourceCreate(BaseModel):
    resource_type: str
    text: Optional[dict] = None
    identifier: Optional[list] = None


class Resource(ResourceCreate):
    id: str
