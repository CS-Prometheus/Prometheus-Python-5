import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import fib, fib_cached, fib_memo


def test_fib_base_cases():
    assert fib(0) == 0
    assert fib(1) == 1


def test_fib_small_values():
    assert fib(5) == 5
    assert fib(10) == 55


def test_fib_cached_matches_naive_small():
    assert fib_cached(10) == 55


def test_fib_cached_handles_large_n_quickly():
    # This would take an extremely long time unmemoized.
    assert fib_cached(35) == 9227465


def test_fib_memo_matches_naive_small():
    assert fib_memo(10) == 55


def test_fib_memo_handles_large_n_quickly():
    assert fib_memo(35) == 9227465
