"""
Exercise 07 — Climbing Stairs (Homework)

TODO: once climb_stairs is working, note the value of climb_stairs(20)
here in this docstring.
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def climb_stairs(n):
    """Return the number of distinct ways to climb n steps, taking 1-3 at a time."""
    # TODO: base case -- n < 0
    # TODO: base case -- n == 0
    # TODO: recursive case -- sum of the three smaller subproblems
    pass
