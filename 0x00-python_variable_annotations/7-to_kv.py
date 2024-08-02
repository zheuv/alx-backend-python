#!/usr/bin/python3
from typing import Tuple
from math import sqrt

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, sqrt(v))
