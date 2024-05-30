# -*- coding: utf-8 -*-
"""Book models."""
from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Model


class Book(Model):
    """Book model."""

    __tablename__ = "book_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(255))
    price: Mapped[str] = mapped_column(String(255))
    date: Mapped[str] = mapped_column(String(255))

    def __init__(self, title, author=None, price=None, date=None):
        """
        Initialize a Book instance.

        :param title: The title of the book.
        :param author: The author of the book (optional).
        :param price: The price of the book (optional).
        :param date: The year the book was published (optional).
        """
        self.title = title
        self.author = author
        self.price = price
        self.date = date

    def __repr__(self):
        """
        Return a string representation of the Book instance.

        :return: A string representation of the book.
        """
        return f"<Book {self.title}>"
