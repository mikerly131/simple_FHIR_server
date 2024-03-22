"""
Routes for making, getting, updating and searching appointments
"""
from fastapi import APIRouter
from schema.appointment import Appointment, AppointmentCreate

router = APIRouter()


# Search for appointments using parameters
@router.get("/Appointment")
def search_appointments(_id: str | None = None, _start_time: str | None = None):
    if _id is None and _start_time is None:
        return {"error": "include a search parameter"}
    else:
        return { "message": "appointment search results", "_id": _id}


# Get an appointment by its unique resource id
@router.get("/Appointment/{id}", response_model=Appointment)
def get_appointment(id: str):
    return {"message": "appointment info", "resource_id": id}


# Create a new appointment
@router.post("/Appointment")
def create_appointment(appointment: AppointmentCreate):
    return {"message": "appointment created"}


@router.put("/Appointment/{id}")
def update_appointment(id: str):
    return {"message": "appointment updated"}


@router.post("/AppointmentResponse")
def confirm_appointment():
    return {"message": "response to appointment accepted"}