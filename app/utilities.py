import hashlib


def _hash_function(value):
    """Hash Function"""
    return hashlib.md5(value.encode("utf-8")).hexdigest()


def generate_password_hash(password):
    return _hash_function(password)
