# -*- coding: utf-8 -*-
"""
Schemas for Book models.

This module contains Pydantic schemas used for validating and serializing
data related to Book models.
"""

from typing import Optional

from pydantic import BaseModel


class BookSchema(BaseModel):
    """Schema for Book model."""

    id: int
    title: str
    author: Optional[str] = None
    price: Optional[str] = None
    date: Optional[str] = None

    class Config:
        """Pydantic configuration for BookSchema."""

        from_attributes = True


class BookCreateSchema(BaseModel):
    """Schema for creating a Book."""

    title: str
    author: Optional[str] = None
    price: Optional[str] = None
    date: Optional[str] = None


class BookUpdateSchema(BaseModel):
    """Schema for updating a Book."""

    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[str] = None
    date: Optional[str] = None
