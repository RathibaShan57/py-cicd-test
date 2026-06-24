"""Tests for the calculator module."""
import pytest
from src.calculator import add, subtract, multiply, divide, power, is_even


class TestAdd:
    def test_positive(self):
        assert add(2, 3) == 5

    def test_negative(self):
        assert add(-1, -4) == -5

    def test_float(self):
        assert add(1.5, 2.5) == pytest.approx(4.0)

    def test_zero(self):
        assert add(0, 0) == 0


class TestSubtract:
    def test_basic(self):
        assert subtract(10, 3) == 7

    def test_negative_result(self):
        assert subtract(3, 10) == -7


class TestMultiply:
    def test_basic(self):
        assert multiply(4, 5) == 20

    def test_by_zero(self):
        assert multiply(100, 0) == 0

    def test_negative(self):
        assert multiply(-3, 4) == -12


class TestDivide:
    def test_basic(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(7, 2) == pytest.approx(3.5)

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)


class TestPower:
    def test_square(self):
        assert power(3, 2) == 9

    def test_zero_exp(self):
        assert power(5, 0) == 1

    def test_one_exp(self):
        assert power(7, 1) == 7


class TestIsEven:
    def test_even(self):
        assert is_even(4) is True

    def test_odd(self):
        assert is_even(7) is False

    def test_zero(self):
        assert is_even(0) is True
