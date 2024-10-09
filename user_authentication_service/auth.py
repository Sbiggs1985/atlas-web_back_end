#!/usr/bin/env python3
"""Auth class"""

from db import DB
from user import User
import bcrypt
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """Hash password."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate UUID."""
    return str(uuid4())


class Auth:
    """Auth: authentication database."""

    def __init__(self):
        self._db = DB()

    def _find_user(self, **kwargs) -> User:
        """Find user by criteria."""
        try:
            return self._db.find_user_by(**kwargs)
        except NoResultFound:
            raise ValueError(f"No user found with {kwargs}")

    def register_user(self, email: str, password: str) -> User:
        """Register a new user."""
        if self._db.find_user_by(email=email):
            raise ValueError(f"User {email} already exists")
        return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Check if login credentials are valid."""
        try:
            user = self._find_user(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except ValueError:
            return False

    def create_session(self, email: str) -> str:
        """Create a session for a user."""
        try:
            user = self._find_user(email=email)
            sess_id = _generate_uuid()
            self._db.update_user(user.id, session_id=sess_id)
            return sess_id
        except ValueError:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """Get user email from session ID."""
        if not session_id:
            return None
        try:
            user = self._find_user(session_id=session_id)
            return user.email
        except ValueError:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy the session of a user."""
        try:
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """Generate and set a reset password token."""
        user = self._find_user(email=email)
        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the user's password using the reset token."""
        user = self._find_user(reset_token=reset_token)
        self._db.update_user(user.id, hashed_password=_hash_password(password),
                             reset_token=None)
