#!/usr/bin/env python3
"""A class that inherits from Auth"""

import base64
from typing import TypeVar
from models.user import User
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class, inherits from Auth"""

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """Returns the Base64 part of the Authorization header"""
        if (authorization_header and isinstance(authorization_header, str) and
                authorization_header.startswith('Basic ')):
            return authorization_header.split(' ', 1)[1]
        return None

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Decodes the Base64 encoded string"""
        if (base64_authorization_header and
                isinstance(base64_authorization_header, str)):
            try:
                return base64.b64decode(
                    base64_authorization_header
                ).decode('utf-8')
            except Exception:
                return None
        return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """Extracts the user email and password from the Base64 decoded value"""
        if (decoded_base64_authorization_header and
                isinstance(decoded_base64_authorization_header, str) and
                ':' in decoded_base64_authorization_header):
            return decoded_base64_authorization_header.split(':', 1)
        return None, None

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """Returns the User instance based on their email and password"""
        if user_email and isinstance(user_email, str) and user_pwd and isinstance(user_pwd, str):
            try:
                users = User.search({'email': user_email})
                for user in users:
                    if user.is_valid_password(user_pwd):
                        return user
            except Exception:
                return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user based on the request's Authorization header"""
        if not request:
            return None
        auth_header = self.authorization_header(request)
        b64_header = self.extract_base64_authorization_header(auth_header)
        decoded_header = self.decode_base64_authorization_header(b64_header)
        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        return self.user_object_from_credentials(user_email, user_pwd)
