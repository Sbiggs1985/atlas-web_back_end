#!/usr/bin/env python3
"""
Using the functions and imports
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Importing asyncio and from task 3
    """
    listDelay = [task_wait_random(max_delay) for i in range(n)]
    inOrder = []
    for delay in asyncio.as_completed(listDelay):
        inOrder.append(await delay)
    return inOrder
