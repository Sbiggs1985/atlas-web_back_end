#!/usr/bin/env python3
""" Writing a String to Redis """

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count number of method calls."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to log the input and output of the method."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key, output_key = method.__qualname__ + \
            ":inputs", method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


class Cache:
    """Cache class to count method calls and track call history."""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data with a randomly generated key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def replay(self, method: Callable):
        """Display history of inputs and outputs for a method."""
        input_key, output_key = method.__qualname__ + \
            ":inputs", method.__qualname__ + ":outputs"
        inputs, outputs = self._redis.lrange(input_key, 0, -1), \
            self._redis.lrange(output_key, 0, -1)

        print(f"{method.__qualname__} was called {len(inputs)} times:")
        for inp, out in zip(inputs, outputs):
            print(f"{method.__qualname__}(*{inp.decode('utf-8')}) -> \
                {out.decode('utf-8')}")
