"""
Main to run web app
"""
from dotenv import load_dotenv

load_dotenv()

import logging
from fastapi import FastAPI
from routes import appointment

logging.basicConfig(level=logging.INFO,
                    filename='app_errors.log',
                    filemode='a',
                    format='%(name)s - %(levelname)s - %(message_s')

app = FastAPI()

app.include_router(appointment.router)
