import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import can_segment


def test_can_segment_true_case():
    assert can_segment("pythoncode", {"python", "code"}) is True


def test_can_segment_false_case():
    assert can_segment("pythonxyz", {"python", "code"}) is False


def test_can_segment_single_word():
    assert can_segment("code", {"python", "code"}) is True


def test_can_segment_multiple_valid_splits():
    assert can_segment("catsanddog", {"cat", "cats", "and", "sand", "dog"}) is True


def test_can_segment_empty_string():
    assert can_segment("", {"python", "code"}) is True
