#!/usr/bin/env python3
"""A class that inherits from Auth"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar

class BasicAuth(Auth):
    """BasicAuth inherits from Auth"""
