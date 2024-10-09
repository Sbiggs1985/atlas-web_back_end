#!/usr/bin/env python3

"""
Coroutine that yields a random number between 0 and 10
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Importing asyncio and random
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
