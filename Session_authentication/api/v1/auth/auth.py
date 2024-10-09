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
        """This checks for the path"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        normal_path = path if path.endswith("/") else path + "/"
        for excluded_path in excluded_paths:
            if excluded_path.endswith("/"):
                if normal_path == excluded_path:
                    return False
            else:
                if path.startwith(excluded_path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """A public method for auth"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """A public method for auth"""
        return None
