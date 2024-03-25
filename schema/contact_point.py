"""
Pydantic model for contact points which many attributes use as a type
"""
from pydantic import BaseModel
from typing import Optional
from enum import Enum


class ContactSystem(str, Enum):
    phone = 'phone'
    fax = 'fax'
    email = 'email'
    pager = 'pager'
    url = 'url'
    sms = 'sms'
    other = 'other'


class ContactUse(str, Enum):
    home = 'home'
    work = 'work'
    temp = 'temp'
    old = 'old'
    mobile = 'mobile'


class ContactPoint(BaseModel):
    system: Optional[ContactSystem] = None
    value: Optional[str] = None
    use: Optional[ContactUse] = None
    rank: Optional[int] = None
    period: Optional[dict[str, str]] = None
