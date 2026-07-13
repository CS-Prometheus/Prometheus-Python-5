import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import coin_change


def test_coin_change_exact_single_coin():
    assert coin_change([1, 5, 10], 10) == 1


def test_coin_change_needs_multiple_coins():
    assert coin_change([1, 5, 10], 12) == 3  # 10 + 1 + 1


def test_coin_change_classic_case():
    assert coin_change([1, 2, 5], 11) == 3  # 5 + 5 + 1


def test_coin_change_zero_amount():
    assert coin_change([1, 2, 5], 0) == 0


def test_coin_change_impossible():
    assert coin_change([2, 5], 3) == -1
