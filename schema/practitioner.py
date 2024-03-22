"""
The pydantic model for provider resource based on FHIR R4 specification.
"""
from resource import Resource
from typing import Optional


class Practitioner(Resource):
