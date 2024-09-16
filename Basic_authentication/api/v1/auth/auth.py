#!/usr/bin/env python3
"""Creating a Authorization Class"""

# api/v1/auth/auth.py

from flask import request
from typing import List, TypeVar

# Creating a generic 'User' TypeVar for future user management
User = TypeVar('User')


class Auth:
    """Checks the authorization"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """This checksfor the path"""
        return False

    def authorization_header(self, request=None) -> str:
        """A public method for auth"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """A public method for auth"""
        return None
