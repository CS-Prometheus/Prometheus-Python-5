import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import power


def test_power_base_case():
    assert power(5, 0) == 1


def test_power_small():
    assert power(2, 1) == 2
    assert power(2, 2) == 4


def test_power_even_exponent():
    assert power(2, 10) == 1024


def test_power_odd_exponent():
    assert power(3, 13) == 1594323
