#!/usr/bin/env python3
"""
Module Doc
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function Doc
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
