#!/usr/bin/env python3
"""Creating a Authorization Class"""

# api/v1/auth/auth.py

from flask import request
from typing import List, TypeVar

# Creating a generic 'User' TypeVar for future user management
User = TypeVar('User')


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the given path requires authentication.
        Currently returns False.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns None for now.
        """
        return None

    def current_user(self, request=None) -> User:
        """
        Returns None for now.
        """
        return None
