"""
Script to populate DB with some test practitioners
"""
from schema.practitioner import PractitionerCreate
from models.practitioner import Practitioner
from db.db import Session

p1 = PractitionerCreate(active=True,
                         name=[{"use": "official", "family": "Henderson", "given": ["Henry"], "prefix": "Dr."},
                               {"use": "usual", "given": ["Hank"]}],
                         telecom=[{"use": "home"}],
                         address=[{"use": "home"}],
                         gender="male",
                         birth_date="1985-07-09")

p2 = PractitionerCreate(active=True,
                         name=[{"use": "official", "family": "Persona", "given": ["Emily"], "prefix": "Dr."},
                               {"use": "maiden", "family": "Nonpersona"}],
                         telecom=[{"use": "home"}],
                         address=[{"use": "home"}],
                         gender="female",
                         birth_date="1962-04-12")

p3 = PractitionerCreate(active=True,
                         name=[{"use": "official", "family": "Testdoc", "given": ["Christina"], "prefix": "Dr."},
                               {"use": "usual", "given": ["Tina"]}],
                         telecom=[{"use": "home"}],
                         address=[{"use": "home"}],
                         gender="female",
                         birth_date="1978-02-23")

prac_data = [p1, p2, p3]


def create_practitioner(p_data: PractitionerCreate) -> Practitioner:
    resource_data = p_data.model_dump()
    return Practitioner(resource_data=resource_data)


if __name__ == "__main__":

    prac_model_data = [create_practitioner(prac) for prac in prac_data]

    session = Session()
    try:
        session.add_all(prac_model_data)
        session.commit()
    except Exception as e:
        print(f"And error occurred: {e}")
        session.rollback()
    finally:
        session.close()

