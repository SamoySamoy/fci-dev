# -*- coding: utf-8 -*-
"""Author models."""
from __future__ import annotations

from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database import Model


class Author(Model):
    """Author model."""

    __tablename__ = "author_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    info: Mapped[str] = mapped_column(String(255))
    books: Mapped[List["Book"]] = relationship(back_populates="author")

    def __init__(self, name: str, info: str = None):
        """
        Initialize an Author instance.

        :param name: The name of the author.
        :param info: Additional information about the author (optional).
        """
        self.name = name
        self.info = info

    def __repr__(self) -> str:
        """
        Return a string representation of the Author instance.

        :return: A string representation of the author.
        """
        return f"<Author {self.name}>"
