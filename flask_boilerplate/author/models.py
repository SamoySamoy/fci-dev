# -*- coding: utf-8 -*-
"""Author models."""
from __future__ import annotations
from typing import List, Optional
import datetime as dt
from flask_boilerplate.database import db, Model
from flask_boilerplate.book.models import Book
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey



class Author(Model):
    """Author model."""

    __tablename__ = "author_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    info: Mapped[str]
    books: Mapped[List["Book"]] = relationship(back_populates="author")
    

    def __init__(self, name, infor=None):
        self.name = name
        self.info = info

    def __repr__(self):
        return f"<Author {self.name}>"
