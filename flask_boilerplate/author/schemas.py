from datetime import datetime
from typing import Optional, Type

from pydantic import BaseModel


class AuthorSchema(BaseModel):
    id: int
    name: str
    info: str = None

    class Config:
        from_attributes = True


class AuthorCreateSchema(BaseModel):
    name: str
    info: Optional[str] = None


class AuthorUpdateSchema(BaseModel):
    name: Optional[str] = None
    info: Optional[str] = None
