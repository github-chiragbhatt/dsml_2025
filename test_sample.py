# test_sample.py
# import pytest
from main import *
# def add(a, b):
#     return a + b


def test_add():
        assert add_two_values(2, 3) == 5  # Test passes
        assert add_two_values(1, 1) == 2  # Test passes
        # assert add_two_values(0, 0) == 1  # Test fails
        assert add_two_values(0, 0) == 0  # Test passes

def test_sub():
        assert subs_two_values(5, 3) == 2

def test_div():
        assert div_two_values(30, 10) == 3 