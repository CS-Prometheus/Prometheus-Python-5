import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import climb_stairs


def test_climb_stairs_zero():
    assert climb_stairs(0) == 1


def test_climb_stairs_small_values():
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 4


def test_climb_stairs_twenty():
    assert climb_stairs(20) == 121415
