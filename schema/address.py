"""
Pydantic model for address which many attributes use as a type
"""
from pydantic import BaseModel
from typing import Optional
from enum import Enum


class AddressUse(str, Enum):
    home = 'home'
    work = 'work'
    temp = 'temp'
    old = 'old'
    billing = 'billing'


class AddressType(str, Enum):
    postal = 'postal'
    physical = 'physical'
    both = 'both'


class Address(BaseModel):
    use: Optional[AddressUse] = None
    type: Optional[AddressType] = None
    text: Optional[str] = None
    line: Optional[list[str]] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    period: Optional[dict[str, str]] = None
