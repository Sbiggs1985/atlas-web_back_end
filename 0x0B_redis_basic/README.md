<h1>Redis Basic</h1>

<p>Redis is an in-memory data structure store, often used as a database, cache, or message broker. Python provides several libraries to interact with Redis, with redis-py being the most popular.</p>

<h2>Learning Objective</h2>
<ul>
  <li>Learn how to use redis for basic operations</li>
  <li>Learn how to use redis as a simple cache</li>
</ul>

<h3>Resources</h3>
<ul>
  <li>Redis Commands</li>
  <li>Redis Python Client</li>
  <li>How to use Redis with Python</li>
  <li>Redis Crash Course Tutorial</li>
</ul>

<h3>Tasks</h3>

<p>Task 3</p>
<p>#!/usr/bin/env python3
""" Writing a String to Redis """

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

"""Task 3"""


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function.
    Args: method: The method to decorate.
    Returns: A wrapped function.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


"""Task 0"""


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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

    # Store some data and check the input/output history
    cache.store(b"first")
    cache.store(b"second")
    cache.store(b"third")

    # Retrieve history of inputs and outputs for Cache.store
    inputs = cache._redis.lrange("Cache.store:inputs", 0, -1)
    outputs = cache._redis.lrange("Cache.store:outputs", 0, -1)

    print("Inputs:", inputs)
    print("Outputs:", outputs)
</p>
