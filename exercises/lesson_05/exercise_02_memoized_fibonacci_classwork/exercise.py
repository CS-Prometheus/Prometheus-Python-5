"""
Exercise 02 — Memoized Fibonacci (Classwork)

TODO (Part C): Explain here, in a few sentences, why fib(35) is fast once
memoized but slow without it. Talk about how many times the naive version
recomputes the same subproblems.
"""

from functools import lru_cache


def fib(n):
    """Naive exponential-time recursive Fibonacci."""
    # TODO: base cases for n == 0 and n == 1
    # TODO: recursive case
    pass


@lru_cache(maxsize=None)
def fib_cached(n):
    """Fibonacci memoized with functools.lru_cache."""
    # TODO: same logic as fib, but this version should be fast for n=35
    pass


def fib_memo(n, memo=None):
    """Fibonacci memoized by hand with a dictionary."""
    if memo is None:
        memo = {}
    # TODO: check memo, base cases, recursive case, store in memo
    pass
