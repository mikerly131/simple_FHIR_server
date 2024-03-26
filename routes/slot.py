"""
Routes for creating, reading, updating and deleting slots

Rules:
- belongs to a specific schedule for a Practitioner or Location
"""
from fastapi import APIRouter
from schema.slot import Slot, SlotCreate

router = APIRouter()


@router.get("/Slot")
def search_slots(_id: str | None = None, _serv_cat: str | None = None):
    if _id is None and _serv_cat is None:
        return {"error": "include a search parameter"}
    else:
        return { "message": "slot search results", "_id": _id}


# Get an slot by its unique resource id
@router.get("/Slot/{id}", response_model=Slot)
def get_slot(id: str):
    return {"message": "slot info", "resource_id": id}


# Create a new slot
@router.post("/Slot")
def create_slot(slot: SlotCreate):
    return {"message": "slot created"}


# Update a slot's information
@router.put("/Slot/{id}")
def update_slot(id: str):
    return {"message": "slot updated"}
