# -*- coding: utf-8 -*-
"""Book views. """
from flask import Blueprint, request, jsonify
from .models import Book
from pydantic import ValidationError
from flask_boilerplate.extensions import db
from .schemas import (
    BookSchema,
    BookCreateSchema,
    BookUpdateSchema,
)

# from .utils import book_to_dict, books_to_dict

blueprint = Blueprint("book", __name__, url_prefix="/books", static_folder="../static")


@blueprint.route("/", methods=["GET"])
def get_all_books():
    books = db.session.scalars(db.select(Book).order_by(Book.id)).all()
    books_pydantic = [BookSchema.from_orm(book).model_dump() for book in books]
    return jsonify(books_pydantic)


@blueprint.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = db.session.scalars(db.select(Book).where(Book.id == book_id)).all()[0]
    book_pydantic = BookSchema.from_orm(book).model_dump()
    return jsonify(book_pydantic)


@blueprint.route("/", methods=["POST"])
def create_book():
    data = request.json

    try:
        book_schema = BookCreateSchema(**data)
        book = Book(**book_schema.dict())
        db.session.add(book)
        db.session.commit()
        return jsonify({"message": "Book created successfully", "id": book.id})
    except ValidationError as e:
        print(e.errors())
        return jsonify({"error": "Invalid payload", "details": e.errors()})


@blueprint.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = db.session.scalars(db.select(Book).where(Book.id == book_id)).all()[0]
    data = request.json

    try:
        book_schema = BookUpdateSchema(**data)
        books = book_schema.dict(exclude_unset=True)
        for key, value in books.items():
            setattr(book, key, value)
        db.session.commit()
        return jsonify({"message": "Book updated successfully"})
    except ValidationError as e:
        print(e.errors())
        return jsonify({"error": "Invalid payload", "details": e.errors()})


@blueprint.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = db.session.scalars(db.select(Book).where(Book.id == book_id)).all()[0]
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"})
