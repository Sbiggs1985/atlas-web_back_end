#!/usr/bin/env python3

"""
Using the code from wait_n and alter it.
Imports asyncio
"""


import asyncio
from your_previous_file import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))
