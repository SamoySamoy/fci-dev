# -*- coding: utf-8 -*-
"""Home views."""
from flask import Blueprint, jsonify

blueprint = Blueprint("public", __name__, url_prefix="/")


@blueprint.route("/", methods=["GET"])
def home():
    """Home views."""
    return jsonify([]), 200
