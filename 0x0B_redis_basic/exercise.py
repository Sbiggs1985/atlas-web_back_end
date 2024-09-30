#!/usr/bin/env python3
""" Writing a String to Redis """

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data with a randomly generated key and return key.

        Args:
            data: The data to store in Redis. Can be str, bytes, int, or float.

        Returns:
            str: The randomly generated key used to store the data.
        """
        # Generate a random key using uuid
        random_key = str(uuid.uuid4())

        # Store the data in Redis using the generated key
        self._redis.set(random_key, data)

        # Return the generated key
        return random_key
