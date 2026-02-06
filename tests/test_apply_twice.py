import pytest
from apply_twice import apply_twice


def test_increment():
    assert apply_twice(lambda x: x + 1, 5) == 7


def test_double():
    assert apply_twice(lambda x: x * 2, 3) == 12


def test_square():
    assert apply_twice(lambda x: x * x, 2) == 16


def test_zero():
    assert apply_twice(lambda x: x + 10, 0) == 20


def test_negative():
    assert apply_twice(lambda x: x - 1, 10) == 8
