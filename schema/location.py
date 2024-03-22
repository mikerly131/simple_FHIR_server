"""
The pydantic model for location resource based on FHIR R4 specification.

Locations will have schedules with slots, and be used for appointments.
"""
from resource import Resource
from typing import Optional


class Location(Resource):
