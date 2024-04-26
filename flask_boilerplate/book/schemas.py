from pydantic import BaseModel
from datetime import datetime


class BookSchema(BaseModel):
    title: str
    author: str
    genre: str | None
    published_year: int | None

    class Config:
        from_attributes = True


class BookCreateSchema(BaseModel):
    title: str
    author: str
    genre: str = None
    published_year: int = None


class BookUpdateSchema(BaseModel):
    title: str = None
    author: str = None
    genre: str = None
    published_year: int = None
