# -*- coding: utf-8 -*-
"""Book views. """
from flask import Blueprint, render_template, request, jsonify
from flask_boilerplate.book.models import Book
from flask_boilerplate.book.schemas import BookSchema, book_orm_to_schema, books_orm_to_schema

blueprint = Blueprint("book", __name__, url_prefix="/books", static_folder="../static")


@blueprint.route("/", methods=["GET"])
def get_all_books():
    books = Book.query.all()
    return jsonify(BookSchema.books_orm_to_schema(books))


@blueprint.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(BookSchema.book_orm_to_schema(book))


@blueprint.route("/", methods=["POST"])
def create_book():
    data = request.json
    book_schema = BookSchema(**data)
    if book_schema.validate():
        book = Book(**book_schema.dict())
        db.session.add(book)
        db.session.commit()
        return jsonify({"message": "Book created successfully", "id": book.id}), 201
    else:
        return jsonify({"error": "Invalid payload", "details": book_schema.errors}), 400


@blueprint.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.json
    book_schema = BookSchema(**data)
    if book_schema.validate():
        book_data = book_schema.dict(exclude_unset=True)
        for key, value in book_data.items():
            setattr(book, key, value)
        db.session.commit()
        return jsonify({"message": "Book updated successfully"})
    else:
        return jsonify({"error": "Invalid payload", "details": book_schema.errors}), 400


@blueprint.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"})
