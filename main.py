"""
Main to run web app
"""
from fastapi import FastAPI
from routes import appointment

app = FastAPI()

app.include_router(appointment.router)
