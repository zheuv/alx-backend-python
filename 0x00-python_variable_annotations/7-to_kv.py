#!/usr/bin/env python3
"""
Module Doc
"""

from typing import Tuple, Union
from math import sqrt


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function Doc
    """
    return (k, sqrt(v))
