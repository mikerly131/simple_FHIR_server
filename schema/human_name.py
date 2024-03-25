"""
Pydantic model for human name since its a varying object
"""
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class NameUse(str, Enum):
    usual = 'usual'
    official = 'official'
    temp = 'temp'
    nickname = 'nickname'
    anonymous = 'anonymous'
    old = 'old'
    maiden = 'maiden'


class HumanName(BaseModel):
    use: NameUse
    text: Optional[str] = None
    family: Optional[str] = None
    given: Optional[list[str]] = None
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    period: Optional[dict[str, str]] = None
