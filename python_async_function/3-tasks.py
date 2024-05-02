#!/usr/bin/env python3

"""
A function (not async) that takes an integer and returns asyncio.Task.
Imports asyncio, a module in Python that provides tools for using async.
"""


import asyncio
from your_previous_file import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))
