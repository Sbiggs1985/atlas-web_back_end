#!/usr/bin/env python3
"""A function to encrypt using bcrypt"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypting passwords"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """This fuction validates the password and decodes it"""
    password = password.encode('utf-8')
    return bcrypt.checkpw(password, hashed_password)
