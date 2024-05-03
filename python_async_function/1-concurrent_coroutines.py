#!/usr/bin/env python3
"""
Importing asyncio and heapq
"""
import asyncio
import heapq
from wait_random import wait_random  # Assuming this import works in your setup


async def wait_n(n: int, max_delay: int) -> list:
    """
    Spawns `wait_random` `n` times with a specified `max_delay`.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)

    heap = []
    for delay in delays:
        heapq.heappush(heap, delay)

    sorted_delays = [heapq.heappop(heap) for _ in range(len(heap))]
    return sorted_delays
