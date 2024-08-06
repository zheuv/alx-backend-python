#!/usr/bin/env python3
"""
Doc for task 1
"""

import asyncio
import random
from typing import List

async def async_generator() -> List[float]:
    
    """
    Coroutine that loops 10 times, each time asynchronously waits 1 second,
    then yields a random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)    
