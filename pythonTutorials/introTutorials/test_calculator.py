from calculator import square
import pytest

def test_square():
    assert square(2) == square(-2)
    assert square(3) == square(-3)
    assert square(0) == 0
