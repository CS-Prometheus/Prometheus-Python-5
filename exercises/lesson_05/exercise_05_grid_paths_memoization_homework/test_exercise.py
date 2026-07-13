import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import count_paths


def test_count_paths_single_row():
    assert count_paths(1, 5) == 1


def test_count_paths_single_column():
    assert count_paths(5, 1) == 1


def test_count_paths_three_by_three():
    assert count_paths(3, 3) == 6


def test_count_paths_four_by_four():
    assert count_paths(4, 4) == 20
