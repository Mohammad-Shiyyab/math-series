import pytest 
# from series.series.py import fibonacci
from series.series import fibonacci
from series.series import lucas
from series.series import sum_series


def test_zero():
    actual = fibonacci(0)
    expected=0
    assert actual ==expected

def test_one():
    actual = fibonacci(1)
    expected=1
    assert actual ==expected

def test_two():
    actual = fibonacci(2)
    expected=1
    assert actual ==expected

def test_three():
    actual = fibonacci(3)
    expected=2
    assert actual ==expected





def test_locas_zero():
    actual = lucas(0)
    expected=2
    assert actual ==expected

def test_locas_one():
    actual = lucas(1)
    expected=1
    assert actual ==expected

def test_locas_two():
    actual = lucas(2)
    expected=3
    assert actual ==expected

def test_locas_three():
    actual = lucas(3)
    expected=4
    assert actual ==expected


def test_sum_zero():
    actual = sum_series(0)
    expected=0
    assert actual ==expected

def test_sum_one():
    actual = sum_series(1)
    expected=1
    assert actual ==expected

def test_sum_two():
    actual = sum_series(2)
    expected=1
    assert actual ==expected

def test_sum_three():
    actual = sum_series(3)
    expected=2
    assert actual == expected
