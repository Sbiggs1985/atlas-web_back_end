#!/usr/bin/env python3
"""
This is a pain in the butt
"""
import asyncio
import heapq
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waiting for this to be done.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = await asyncio.gather(*tasks)

    heap: List[float] = []
    for delay in delays:
        heapq.heappush(heap, delay)
    sorted_delays = [heapq.heappop(heap) for _ in range(len(heap))]
    return sorted_delays
