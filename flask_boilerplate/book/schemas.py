from pydantic import BaseModel, Field
from datetime import datetime
from flask_boilerplate.book.models import Book


class BookSchema(BaseModel):
    title: str = Field(..., description="Title of the book")
    author: str = Field(..., description="Author of the book")
    genre: str = Field(None, description="Genre of the book")
    created_at: datetime = Field(
        ..., description="Created date of the book in database"
    )
    
    published_year: int = Field(None, description="Published year of the book")

    class Config:
        orm_mode = True


def book_orm_to_schema(book: Book) -> BookSchema:
    return BookSchema(
        title=book.title,
        author=book.author,
        genre=book.genre,
        published_year=book.published_year,
    )


def books_orm_to_schema(books: list[Book]) -> list[BookSchema]:
    return [book_orm_to_schema(book) for book in books]
