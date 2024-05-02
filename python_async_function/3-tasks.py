#!/usr/bin/env python3

"""
A function (not async) that takes an integer and returns asyncio.Task.
"""


import asyncio
from your_previous_file import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Using the task_wait_random function
    """
    return asyncio.create_task(wait_random(max_delay))
