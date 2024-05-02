from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Type, TypeVar


class BookSchema(BaseModel):
    id: int
    title: str
    author_id: int = None
    genre: str = None
    published_year: str = None

    class Config:
        from_attributes = True


class BookCreateSchema(BaseModel):
    title: str
    author_id: Optional[int] = None
    genre: Optional[str] = None
    published_year: Optional[str] = None


class BookUpdateSchema(BaseModel):
    title: Optional[str] = None
    author_id: Optional[int] = None
    genre: Optional[str] = None
    published_year: Optional[str] = None
