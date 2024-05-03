#!/usr/bin/env python3
"""
This is a pain in the butt
"""
import asyncio
import heapq
from my_wait_random import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Waiting for this to be done.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = await asyncio.gather(*tasks)

    heapq = []
    for delay in delays:
        heapq.heappush(heap, delay)
    sorted_delays = [heapq.heappop(heap) for _ in range(len(heap))]
    return sorted_delays
