"""
Routes for creating, reading, updating and deleting schedules

Rules:
- belongs to one instance of a resource: Practitioner or Location in this systems
- will create, update or delete Slot resources
"""
from fastapi import APIRouter
from schema.schedule import Schedule, ScheduleCreate
from schema.slot import Slot, SlotCreate

router = APIRouter()


# note, bundles expected return resource
@router.get("/Schedule")
def search_schedules(_id: str | None = None, _serv_cat: str | None = None):
    if _id is None and _serv_cat is None:
        return {"error": "include a search parameter"}
    else:
        return { "message": "schedule search results", "_id": _id}


# Get an schedule by its unique resource id
@router.get("/Schedule/{id}", response_model=Schedule)
def get_schedule(id: str):
    return {"message": "schedule info", "resource_id": id}


# Create a new schedule
@router.post("/Schedule")
def create_schedule(schedule: ScheduleCreate):
    return {"message": "schedule created"}


# Update a schedule's information
@router.put("/Schedule/{id}")
def update_schedule(id: str):
    return {"message": "schedule updated"}
