# -*- coding: utf-8 -*-
"""Author models."""
from __future__ import annotations

import datetime as dt
from typing import List, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_boilerplate.database import Model, db


class Author(Model):
    """Author model."""

    __tablename__ = "author_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    info: Mapped[str] = mapped_column(String(255))
    books: Mapped[List["Book"]] = relationship(back_populates="author")

    def __init__(self, name, info=None):
        self.name = name
        self.info = info

    def __repr__(self):
        return f"<Author {self.name}>"
