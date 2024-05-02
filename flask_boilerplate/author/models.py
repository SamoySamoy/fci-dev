# -*- coding: utf-8 -*-
"""Author models."""
import datetime as dt
from flask_boilerplate.database import db, Model
from sqlalchemy.orm import Mapped, mapped_column


class Author(Model):
    """Author model."""

    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    info: Mapped[str]
    # Establishing a one-to-many relationship between Author and Book
    books = relationship("Book", back_populates="authors")

    def __init__(self, name, infor=None):
        self.name = name
        self.info = info

    def __repr__(self):
        return f"<Author {self.name}>"
