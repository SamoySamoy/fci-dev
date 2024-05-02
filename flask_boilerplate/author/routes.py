# -*- coding: utf-8 -*-
"""author views. """
from flask import Blueprint, request, jsonify
from .models import Author
from pydantic import ValidationError
from flask_boilerplate.extensions import db
from .schemas import (
    AuthorSchema,
    AuthorCreateSchema,
    AuthorUpdateSchema,
)


blueprint = Blueprint(
    "author", __name__, url_prefix="/authors", static_folder="../static"
)


@blueprint.route("/", methods=["GET"])
def get_all_authors():
    authors = db.session.execute(db.select(Author))
    authors_pydantic = [
        AuthorSchema.from_orm(author).model_dump() for author in authors
    ]
    return jsonify(authors_pydantic)


@blueprint.route("/<int:author_id>", methods=["GET"])
def get_author(author_id):
    author = db.get_or_404(Author, author_id)
    author_pydantic = authorSchema.from_orm(author).model_dump()
    return jsonify(author_pydantic)


@blueprint.route("/", methods=["POST"])
def create_author():
    data = request.json
    try:
        author_schema = AuthorCreateSchema(**data)
        author = Author(**author_schema.dict())
        db.session.add(author)
        db.session.commit()
        return jsonify({"message": "author created successfully", "id": author.id})
    except ValidationError as e:
        print(e.errors())
        return jsonify({"error": "Invalid payload", "details": e.errors()})


@blueprint.route("/<int:author_id>", methods=["PUT"])
def update_author(author_id):
    author = db.get_or_404(Author, author_id)
    data = request.json

    try:
        author_schema = AuthorUpdateSchema(**data)
        authors = author_schema.dict(exclude_unset=True)
        for key, value in authors.items():
            setattr(Author, key, value)
        db.session.commit()
        return jsonify({"message": "author updated successfully"})
    except ValidationError as e:
        print(e.errors())
        return jsonify({"error": "Invalid payload", "details": e.errors()})


@blueprint.route("/<int:author_id>", methods=["DELETE"])
def delete_author(author_id):
    author = db.get_or_404(Author, author_id)
    db.session.delete(author)
    db.session.commit()
    return jsonify({"message": "author deleted successfully"})
