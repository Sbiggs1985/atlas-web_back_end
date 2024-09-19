#!/usr/bin/env python3
"""Creating a Authorization Class. P"""

import sys
import os
import base64
from typing import Tuple, Optional
from models.user import User
from api.v1.auth.auth import Auth

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../..')))


class BasicAuth(Auth):
    """BasicAuth class to handle Basic Authentication."""

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> Optional[str]:
        """Extracts the Base64 part of the Authorization header."""
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> Optional[str]:
        """Decodes the Base64 encoded Authorization header."""
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except Exception:
            return None
        return decoded

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[Optional[str], Optional[str]]:
        """Extracts the user credentials."""
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> Optional[User]:
        """Retrieves a User instance from the provided email and password."""
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        user = User.search({'email': user_email})
        if user is None:
            return None

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> Optional[User]:
        """Retrieves the authenticated user based on the request."""
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None

        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if decoded_auth is None:
            return None

        email, password = self.extract_user_credentials(decoded_auth)
        if email is None or password is None:
            return None

        return self.user_object_from_credentials(email, password)
