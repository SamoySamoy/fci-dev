# -*- coding: utf-8 -*-
"""Book views."""
from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from sqlalchemy.exc import NoResultFound

from backend.extensions import db

from .models import Book
from .schemas import BookCreateSchema, BookSchema, BookUpdateSchema

blueprint = Blueprint("book", __name__, url_prefix="/books")


@blueprint.route("/", methods=["GET"])
def get_all_books():
    """Get all books."""
    books = db.session.scalars(db.select(Book).order_by(Book.id)).all()
    books_pydantic = [BookSchema.from_orm(book).model_dump() for book in books]
    return jsonify(books_pydantic), 200


@blueprint.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    """Get a book by ID."""
    try:
        book = db.session.scalars(db.select(Book).where(Book.id == book_id)).all()[0]
        book_pydantic = BookSchema.from_orm(book).model_dump()
        return jsonify(book_pydantic), 200
    except NoResultFound:
        return jsonify({"error": f"Book with ID {book_id} not found"}), 404


@blueprint.route("/", methods=["POST"])
def create_book():
    """Create a new book."""
    data = request.json
    try:
        book_schema = BookCreateSchema(**data)
        book = Book(**book_schema.dict())
        db.session.add(book)
        db.session.commit()
        return jsonify({"message": "Book created successfully", "id": book.id}), 201
    except ValidationError as e:
        return jsonify({"error": "Invalid payload", "details": e.errors()}), 400


@blueprint.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    """Update an existing book."""
    try:
        book = db.session.scalars(db.select(Book).where(Book.id == book_id)).all()[0]
        data = request.json
        book_schema = BookUpdateSchema(**data)
        updates = book_schema.dict(exclude_unset=True)
        for key, value in updates.items():
            setattr(book, key, value)
        db.session.commit()
        return jsonify({"message": "Book updated successfully"}), 200
    except NoResultFound:
        return jsonify({"error": f"Book with ID {book_id} not found"}), 404
    except ValidationError as e:
        return jsonify({"error": "Invalid payload", "details": e.errors()}), 400


@blueprint.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    """Delete a book by ID."""
    try:
        book = db.session.scalars(db.select(Book).where(Book.id == book_id)).all()[0]
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully"}), 200
    except NoResultFound:
        return jsonify({"error": f"Book with ID {book_id} not found"}), 404
