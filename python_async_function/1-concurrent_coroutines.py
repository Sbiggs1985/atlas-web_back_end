#!/usr/bin/env python3

"""
Executing multiple coroutines at the same time with async.
"""


import asyncio
from typing import List
from your_previous_file import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Spawns `wait_random` `n` times
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)

    heap = []
    for delay in delays:
        heapq.heappush(heap, delay)

    sorted_delays = [heapq.heappop(heap) for _ in range(len(heap))]
    return sorted_delays
