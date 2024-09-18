#!/usr/bin/env python3
"""Creating User"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError, NoResultFound
from user import Base, User

VALID_FIELDS = {'id', 'email', 'hashed_password', 'session_id', 'reset_token'}


class DB:
    """DB class."""

    def __init__(self):
        """Constructor."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Session property."""
        if self.__session is None:
            self.__session = sessionmaker(bind=self._engine)()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user."""
        if not email or not hashed_password:
            raise ValueError("Email and hashed_password must be provided")
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find user by attributes."""
        if not kwargs or not set(kwargs.keys()).issubset(VALID_FIELDS):
            raise InvalidRequestError("Invalid field(s) in query")
        session = self._session
        try:
            return session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found with the given criteria")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user attributes."""
        session = self._session
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if k not in VALID_FIELDS:
                raise ValueError(f"Invalid field: {k}")
            setattr(user, k, v)
        session.commit()
