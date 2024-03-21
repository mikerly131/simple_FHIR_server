"""
Routes for making, getting, updating and searching appointments
"""
from fastapi import APIRouter, Request, Depends

router = APIRouter()


# Search for appointments using parameters
@router.get("/Appointment/")
def search_appointments(request: Request, _id: str | None = None):
    return { "message": "appointment search results", "_id": _id}


# Get an appointment by its unique resource id
@router.get("/Appointment/{id}")
def get_appointment(request: Request, id: str):
    return {"message": "appointment info", "resource_id": id}


# Create a new appointment
@router.post("/Appointment")
def create_appointment(request: Request):
    return {"message": "appointment created"}


@router.put("/Appointment/{id}")
def update_appointment(request: Request, id: str):
    return {"message": "appointment updated"}


@router.post("/AppointmentResponse")
def confirm_appointment(request: Request):
    return {"message": ""}