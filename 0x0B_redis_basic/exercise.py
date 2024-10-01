#!/usr/bin/env python3
""" Writing a String to Redis """

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

"""TASK 2"""


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    Args: method: The method to decorate.
    Returns: A wrapped function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        # Call the original method
        return method(self, *args, **kwargs)

    return wrapper


"""Task 0"""


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data with a randomly generated key and return key.
        Args: data: The data to store in Redis.
        Returns: str: The generated key used to store the data.
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
        Retrieve data from Redis, optionally applying a function.
        Args: key: The key for the stored data.
        Returns: The data as bytes converted.
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
        Args: key: The key for the stored data.
        Returns: The data as a decoded string or None.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data as an integer.
        Args: key: The key for the stored data.
        Returns: The data as an integer or None.
        """
        return self.get(key, fn=lambda d: int(d))


if __name__ == "__main__":
    cache = Cache()

    # Test case to store data and check the count of calls
    key1 = cache.store(b"first")
    key2 = cache.store(b"second")
    key3 = cache.store(b"third")

    # Get the number of times 'store' has been called
    print(cache.get(cache.store.__qualname__))  # Should print 3

    # Test retrieving values
    print(cache.get_str(key1))  # Should print "first"
    print(cache.get_str(key2))  # Should print "second"
    print(cache.get_str(key3))  # Should print "third"
