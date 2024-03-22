"""
Pydantic model for codeable concepts which many attributes use as a type
"""
from pydantic import BaseModel, Field
from typing import Optional


class Code(BaseModel):
    code: Optional[str] = Field(None, example="1232")
    display: Optional[str] = Field(None, example="Negative Result")
    system: Optional[str] = Field(None, example="http://snomed.info/sct")


class CodeableConcept(BaseModel):
    coding: Optional[list[Code]] = None
    text: Optional[str] = Field(None, example="Negative Result")

    class Config:
        schema_extra = {
            "coding": [
                {
                    "code": "1232",
                    "display": "Negative Result",
                    "system": "http://snomed.info/sct"
                }
            ],
            "text": "Negative Test Result"
        }
