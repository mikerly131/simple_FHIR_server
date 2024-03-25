"""
Script to populate DB with some test patients
"""
from schema.patient import PatientCreate
from models.patient import Patient
from db.db import Session

patient1 = PatientCreate(active=True,
                         name=[{"use": "official", "family": "Clark", "given": ["James"]},
                               {"use": "usual", "given": ["Jim"]}],
                         telecom=[{"use": "home"}],
                         address=[{"use": "home"}],
                         gender="male",
                         birth_date="1992-10-18",
                         deceased_boolean=False)

patient2 = PatientCreate(active=True,
                         name=[{"use": "official", "family": "Dogg", "given": ["Gooferson"]},
                               {"use": "usual", "given": ["Goofy"]}],
                         telecom=[{"use": "home"}],
                         address=[{"use": "home"}],
                         gender="male",
                         birth_date="1942-03-28",
                         deceased_boolean=False)

patient3 = PatientCreate(active=True,
                         name=[{"use": "official", "family": "Madison", "given": ["Sarah"]}],
                         telecom=[{"use": "home"}],
                         address=[{"use": "home"}],
                         gender="female",
                         birth_date="1979-06-03",
                         deceased_boolean=False)

patient_data = [patient1, patient2, patient3]


def create_patient(patient_data: PatientCreate) -> Patient:
    resource_data = patient_data.model_dump()
    return Patient(resource_data=resource_data)


if __name__ == "__main__":

    patient_model_data = [create_patient(patient) for patient in patient_data]

    session = Session()
    try:
        session.add_all(patient_model_data)
        session.commit()
    except Exception as e:
        print(f"And error occurred: {e}")
        session.rollback()
    finally:
        session.close()

