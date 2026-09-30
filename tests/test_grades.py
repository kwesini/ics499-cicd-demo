"""Tests for src/grades.py. pytest runs every function named test_*."""

import pytest

from src.grades import CUTOFFS, letter_grade


def test_top_grade():
    assert letter_grade(97) == "A"  # assert = "this must be true"


def test_boundary_is_inclusive():
    assert letter_grade(90) == "A-"  # exactly 90 is A-, not B+


def test_failing_grade():
    assert letter_grade(59.9) == "F"


def test_rejects_bad_input():
    with pytest.raises(ValueError):  # passes only if an error happens
        letter_grade(120)


def test_scale_goes_from_highest_to_lowest():
    minimums = [minimum for minimum, _ in CUTOFFS]
    assert minimums == sorted(minimums, reverse=True)
