"""Collection of utility functions"""

import hashlib

import falcon

from . import db
from .exceptions import HTTPError
from .models import User


def find_item_by_id(db, model, id):
    """Helper method to find item or return 404"""
    item = db.query(model).get(id)
    if not item:
        raise HTTPError(falcon.HTTP_404, errors={"id": "does not exist"})
    return item


def generate_password_hash(password):
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def user_loader(payload):
    """Helper method for falcon-auth to load user from decoded JWT payload"""
    user = payload["user"]
    return db.query(User).filter(User.id == user["id"]).first()
