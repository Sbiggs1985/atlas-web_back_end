#!/usr/bin/env python3

"""
Type-annotation function with parameters with values.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random function
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
