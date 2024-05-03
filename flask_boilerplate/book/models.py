# -*- coding: utf-8 -*-
"""Book models."""
from __future__ import annotations
from typing import List, Optional
import datetime as dt
from flask_boilerplate.database import db, Model
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Book(Model):
    """Book model."""

    __tablename__ = "book_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("author_table.id"))
    author: Mapped["Author"] = relationship(back_populates="books")
    genre: Mapped[str]
    published_year: Mapped[str]

    def __init__(self, title, author_id=None, genre=None, published_year=None):
        self.title = title
        self.author_id = author_id
        self.genre = genre
        self.published_year = published_year

    def __repr__(self):
        return f"<Book {self.title}>"
