# -*- coding: utf-8 -*-
"""
Schemas for Author models.

This module contains Pydantic schemas used for validating and serializing
data related to Author models.
"""

from typing import Optional

from pydantic import BaseModel


class AuthorSchema(BaseModel):
    """Schema representing an Author."""

    id: int
    name: str
    info: Optional[str] = None

    class Config:
        """Configuration for AuthorSchema."""

        from_attributes = True


class AuthorCreateSchema(BaseModel):
    """Schema for creating a new Author."""

    name: str
    info: Optional[str] = None


class AuthorUpdateSchema(BaseModel):
    """Schema for updating an existing Author."""

    name: Optional[str] = None
    info: Optional[str] = None
