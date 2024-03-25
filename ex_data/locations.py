"""
Script to populate DB with some test practitioners
"""
from schema.location import LocationCreate
from models.location import Location
from db.db import Session

l1 = LocationCreate(status='active',
                    name='Room 1',
                    alias=['Blue Room'],
                    description='General practice room',
                    physical_type={"coding": [{"code": "ro", "system": "http://hl7.org/fhir/ValueSet/location-physical-type", "display": "Room"}]},
                    telecom=[{"system": "phone", "value": "0001", "use": "work"}],
                    partOf={"reference": "Location/9"})
l2 = LocationCreate(status='active',
                    name='Room 2',
                    alias=['Green Room'],
                    description='General practice room',
                    physical_type={"coding": [{"code": "ro", "system": "http://hl7.org/fhir/ValueSet/location-physical-type", "display": "Room"}]},
                    telecom=[{"system": "phone", "value": "0002", "use": "work"}],
                    partOf={"reference": "Location/9"})
l3 = LocationCreate(status='active',
                    name='Room 3',
                    alias=['Yellow Room'],
                    description='General practice room',
                    physical_type={"coding": [{"code": "ro", "system": "http://hl7.org/fhir/ValueSet/location-physical-type", "display": "Room"}]},
                    telecom=[{"system": "phone", "value": "0003", "use": "work"}],
                    partOf={"reference": "Location/9"})
l4 = LocationCreate(status='active',
                    name='Room 4',
                    alias=['Orange Room'],
                    description='General practice room',
                    physical_type={"coding": [{"code": "ro", "system": "http://hl7.org/fhir/ValueSet/location-physical-type", "display": "Room"}]},
                    telecom=[{"system": "phone", "value": "0004", "use": "work"}],
                    partOf={"reference": "Location/9"})
l5 = LocationCreate(status='active',
                    name='Room 5',
                    alias=['Pink Room'],
                    description='General practice room',
                    physical_type={"coding": [{"code": "ro", "system": "http://hl7.org/fhir/ValueSet/location-physical-type", "display": "Room"}]},
                    telecom=[{"system": "phone", "value": "0005", "use": "work"}],
                    partOf={"reference": "Location/9"})
l6 = LocationCreate(status='active',
                    name='Room 6',
                    alias=['Lavender Room'],
                    description='General practice room',
                    physical_type={"coding": [{"code": "ro", "system": "http://hl7.org/fhir/ValueSet/location-physical-type", "display": "Room"}]},
                    telecom=[{"system": "phone", "value": "0006", "use": "work"}],
                    partOf={"reference": "Location/9"})
l7 = LocationCreate(status='active',
                    name='Room 7',
                    alias=['White Room'],
                    description='Patient and doctor conference room',
                    physical_type={"coding": [{"code": "ro", "system": "http://hl7.org/fhir/ValueSet/location-physical-type", "display": "Room"}]},
                    telecom=[{"system": "phone", "value": "0007", "use": "work"}],
                    partOf={"reference": "Location/9"})
l8 = LocationCreate(status='active',
                    name='Room 8',
                    alias=['Red Room'],
                    description='Blood and specimen collection room',
                    type=[{"coding": [{"code": "HUSCS", "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode", "display": "specimen collection site"}]}],
                    physical_type={"coding": [{"code": "ro", "system": "http://hl7.org/fhir/ValueSet/location-physical-type", "display": "Room"}]},
                    telecom=[{"system": "phone", "value": "0008", "use": "work"},
                             {"system": "fax", "value": "1118", "use": "work"}],
                    partOf={"reference": "Location/9"})
l9 = LocationCreate(status='active',
                    name='Cools Docs Office',
                    alias=['Main Office'],
                    description='Office building for Cool Docs practice',
                    type=[{"coding": [{"code": "PROFF", "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode", "display": "Provider's Office"}]}],
                    physical_type={"coding": [{"code": "bu", "system": "http://hl7.org/fhir/ValueSet/location-physical-type", "display": "Building"}]},
                    telecom=[{"system": "phone", "value": "1-555-555-0000", "use": "work"},
                             {"system": "email", "value": "cooldocs@cooldocs.org"},
                             {"system": "fax", "value": "1-555-555-1110", "use": "work"}],
                    address={"use": "work", "type": "both", "line": ["2201 Doctors Drive"],
                             "city": "Springfield", "state": "NJ", "postal_code": "08043", "country": "USA"})

loc_data = [l1, l2, l3, l4, l5, l6, l7, l8, l9]


def create_location(p_data: LocationCreate) -> Location:
    resource_data = p_data.model_dump()
    return Location(resource_data=resource_data)


if __name__ == "__main__":

    loc_model_data = [create_location(loc) for loc in loc_data]

    session = Session()
    try:
        session.add_all(loc_model_data)
        session.commit()
    except Exception as e:
        print(f"And error occurred: {e}")
        session.rollback()
    finally:
        session.close()

