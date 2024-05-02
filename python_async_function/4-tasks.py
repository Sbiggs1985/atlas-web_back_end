#!/usr/bin/env python3

"""
Using the code from wait_n and alter it.
"""


import asyncio
from your_previous_file import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Using the your_previous_file function
    """
    return asyncio.create_task(wait_random(max_delay))
