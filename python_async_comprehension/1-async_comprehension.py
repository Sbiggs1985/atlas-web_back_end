#!/usr/bin/env python3

"""
Documentation
"""

import asyncio
from typing import List
from async_generator from async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers
    """
    random_numbers: List[float] = [x async for x in async_generator()]

    return random_numbers
