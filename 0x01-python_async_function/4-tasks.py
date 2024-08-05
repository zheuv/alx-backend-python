#!/usr/bin/env python3
"""
Doc for task 5
"""

import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    
    Args:
    n (int): The number of times to spawn task_wait_random.
    max_delay (int): The maximum delay for each task_wait_random.

    Returns:
    list: A list of all delays (float values) in ascending order.
    """
    tasks = [wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
