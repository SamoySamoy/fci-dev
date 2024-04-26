# -*- coding: utf-8 -*-
"""User views."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required

from flask_boilerplate.user.models import User


blueprint = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")


@blueprint.route("/", methods=["GET"])
@login_required
def members():
    """List members."""
    return render_template("users/members.html")


@blueprint.route("/update/<int:user_id>", methods=["GET", "POST"])
@login_required
def update(user_id):
    if request.method == "POST":
        return render_template("user/update.html")
    return render_template("public/home.html")
