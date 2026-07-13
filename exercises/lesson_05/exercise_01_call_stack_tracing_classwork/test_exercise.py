import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import factorial, rec_sum


def test_factorial_base_case():
    assert factorial(0) == 1


def test_factorial_small():
    assert factorial(1) == 1
    assert factorial(3) == 6


def test_factorial_five():
    assert factorial(5) == 120


def test_rec_sum_empty():
    assert rec_sum([]) == 0


def test_rec_sum_single():
    assert rec_sum([7]) == 7


def test_rec_sum_multiple():
    assert rec_sum([1, 2, 3, 4]) == 10
