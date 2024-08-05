#!/usr/bin/env python3
"""
doc of for the task 0
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    uses asyncio to await for a 0 < delay < max_delay
    and returns the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
