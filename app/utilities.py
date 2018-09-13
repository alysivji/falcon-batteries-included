"""Collection of utility functions"""

from passlib.hash import bcrypt

import falcon

from . import db
from .exceptions import HTTPError
from .models import User


def find_by_id(db, model, id, *, worker_task=False):
    """Helper method to find item or return 404 or raise async worker error"""
    item = db.query(model).get(id)
    if not item:
        if worker_task:
            raise RuntimeError("could not find")  # TODO pick better exception
        raise HTTPError(falcon.HTTP_404, errors={"id": "does not exist"})
    return item


def generate_password_hash(password: str) -> str:
    return bcrypt.hash(password)


def password_matches(password: str, hashed_password: str) -> bool:
    return bcrypt.verify(password, hashed_password)


def user_loader(payload):
    """Helper method for falcon-auth to load user from decoded JWT payload"""
    user = payload["user"]
    return db.query(User).filter(User.id == user["id"]).first()
