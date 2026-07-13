import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import flatten


def test_flatten_already_flat():
    assert flatten([1, 2, 3]) == [1, 2, 3]


def test_flatten_one_level():
    assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]


def test_flatten_deeply_nested():
    assert flatten([1, [2, [3, [4]], 5]]) == [1, 2, 3, 4, 5]


def test_flatten_empty_list():
    assert flatten([]) == []


def test_flatten_empty_nested_lists():
    assert flatten([1, [], [2, []], 3]) == [1, 2, 3]
