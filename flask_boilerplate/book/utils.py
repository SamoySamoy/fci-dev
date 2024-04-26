from pydantic import BaseModel, Field
from datetime import datetime
from .models import Book


def book_to_dict(book):
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "published_year": book.published_year,
    }


def books_to_dict(books):
    return [book_to_dict(book) for book in books]
