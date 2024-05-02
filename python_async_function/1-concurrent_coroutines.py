#!/usr/bin/env python3

"""
Executing multiple coroutines at the same time with async.
Imports wait_random from previous Python file.
"""


import asyncio
from typing import List
from your_previous_file import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
