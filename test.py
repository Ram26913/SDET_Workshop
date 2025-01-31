import pytest

def sum(a,b):
    return a+b

def test_sum():
    assert sum(1,2) == 2
    assert sum(2,3) == 5
test_sum()
    