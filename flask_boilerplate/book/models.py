# -*- coding: utf-8 -*-
"""Book models."""
import datetime as dt

from sqlalchemy.ext.hybrid import hybrid_property
from flask_boilerplate.database import Column, PkModel, db, reference_col, relationship
from flask_boilerplate.extensions import bcrypt


class Book(PkModel):
    """Book model."""
    __tablename__ = "books"
    title = Column(db.String(255), nullable=False)
    author = Column(db.String(255), nullable=False)
    genre = Column(db.String(100))
    published_year = Column(db.Integer)
    
    def __init__(self, title, author, genre=None, published_year=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.published_year = published_year

    def __repr__(self):
        return f'<Book {self.title} of {self.author}>'
