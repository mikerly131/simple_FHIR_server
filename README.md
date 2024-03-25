# About
Making a simple, python FHIR server for practice with FHIR resources, APIs

## Planning - Functionality
1. Support for appointment scheduling workflow with FHIR resources.
2. Implement oAuth2 for authentication and security, might need an auth server / app.
3. Add encounters, conditions and requests/orders for tracking appointment outcomes and follow-ups.
4. Implement search capability and terms per FHIR spec for resource endpoints.

## Current Progress
Work on first set of functionality, progress:
* Resource models defined
* DB setup and connected
* Most endpoints/routes stubbed
* Some test data and scripts to load created

### FHIR Resources - Appointment Scheduling
Defined:  Patient, Provider, Location, Appointment, Schedule, Slot  
Not including:  Devices, HealthcareServices

### FHIR API Details
/Appointment - create, read, update, delete, search
/Schedule - create, read, update, search
/Slot - tbc

## Tech Details
Using fastAPI web framework
Postgres DB connected by SQLAlchemy (sync)
Pydantic schema to validate FHIR resource data