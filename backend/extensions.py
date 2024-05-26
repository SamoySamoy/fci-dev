# -*- coding: utf-8 -*-
"""Extension modules initilization."""
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_static_digest import FlaskStaticDigest
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Initial."""

    pass


db = SQLAlchemy(model_class=Base)

bcrypt = Bcrypt()
migrate = Migrate()
cache = Cache()
debug_toolbar = DebugToolbarExtension()
flask_static_digest = FlaskStaticDigest()
