#!/usr/bin/env python3
""" Writing a String to Redis """

import redis
import uuid
from typing import Union, callable, Optional


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
        random_key = str(uuid.uuid4())

        self._redis.set(random_key, data)

        return random_key

    """ *Task* 1"""
    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Union[str, int, bytes, None]]] = None
            ) -> Optional[Union[str, int, bytes]]:
        """
        Retrieve data from Redis, optionally applying a conversion function.

        Args:
            key: The key for the stored data.

        Returns:
            The data as bytes converted.
        """
        value = self._redis.get(key)

        if value is None:
            return None

        if fn is not None:
            return fn(value)

        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data as a UTF-8 decoded string.

        Args:
            key: The key for the stored data.

        Returns:
            The data as a decoded string or None.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data as an integer.

        Args:
            key: The key for the stored data.

        Returns:
            The data as an integer or None if key does not exist.
        """
        return self.get(key, fn=lambda d: int(d))


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

print("All test cases passed!")
