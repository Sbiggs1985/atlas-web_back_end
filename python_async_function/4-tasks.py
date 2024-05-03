#!/usr/bin/env python3

"""
Using the code from wait_n and alter it.
"""


import asyncio
import heapq
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of delays
    """
    tasks: List[asyncio.Task] = [wait_n(max_delay) for _ in range(n)]

    delays: List[float] = await asyncio.gather(*tasks)

    heap: List[float] = []
    for delay in delays:
        heapq.heappush(heap, delay)

    sorted_delays: List[float] = [heapq.heappop(heap) for _ in range(len(heap))]
    return sorted_delays
