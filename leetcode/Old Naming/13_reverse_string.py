"""Reverse a string"""
from typing import List


def reverseString(s: List[str]) -> List[str]:
    return s[-1:-len(s)-1:-1]


reverseString([])
