# -*- coding: utf-8 -*-
"""Author views."""
from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from flask_boilerplate.extensions import db

from .models import Author
from .schemas import AuthorCreateSchema, AuthorSchema, AuthorUpdateSchema

blueprint = Blueprint(
    "author", __name__, url_prefix="/authors", static_folder="../static"
)


@blueprint.route("/", methods=["GET"])
def get_all_authors():
    """Retrieve all authors."""
    authors = db.session.scalars(db.select(Author).order_by(Author.id)).all()

    authors_pydantic = [
        AuthorSchema.from_orm(author).model_dump() for author in authors
    ]
    return jsonify(authors_pydantic), 200


@blueprint.route("/<int:author_id>", methods=["GET"])
def get_author(author_id):
    """Retrieve a single author by ID."""
    try:
        author = db.session.scalars(
            db.select(Author).where(Author.id == author_id)
        ).all()[0]
        author_pydantic = AuthorSchema.from_orm(author).model_dump()
        return jsonify(author_pydantic), 200
    except IndexError:
        return jsonify({"error": f"Author with ID {author_id} not found"}), 404


@blueprint.route("/", methods=["POST"])
def create_author():
    """Create a new author."""
    data = request.json
    try:
        author_schema = AuthorCreateSchema(**data)
        author = Author(**author_schema.dict())
        db.session.add(author)
        db.session.commit()
        return jsonify({"message": "author created successfully", "id": author.id}), 200
    except ValidationError as e:
        print(e.errors())
        return jsonify({"error": "Invalid payload", "details": e.errors()}), 400


@blueprint.route("/<int:author_id>", methods=["PUT"])
def update_author(author_id):
    """Update an existing author."""
    try:
        author = db.session.scalars(
            db.select(Author).where(Author.id == author_id)
        ).all()[0]
    except IndexError:
        return jsonify({"error": f"Author with ID {author_id} not found"}), 404

    data = request.json

    try:
        author_schema = AuthorUpdateSchema(**data)
        updates = author_schema.dict(exclude_unset=True)
        for key, value in updates.items():
            setattr(author, key, value)
        db.session.commit()
        return jsonify({"message": "author updated successfully"}), 200
    except ValidationError as e:
        print(e.errors())
        return jsonify({"error": "Invalid payload", "details": e.errors()}), 400


@blueprint.route("/<int:author_id>", methods=["DELETE"])
def delete_author(author_id):
    """Delete an author by ID."""
    try:
        author = db.session.scalars(
            db.select(Author).where(Author.id == author_id)
        ).all()[0]
        db.session.delete(author)
        db.session.commit()
        return jsonify({"message": "author deleted successfully"}), 200
    except IndexError:
        return jsonify({"error": f"Author with ID {author_id} not found"}), 404
