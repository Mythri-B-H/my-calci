"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""

import pytest
from src.calculator import add, subtract, multiply, divide, power, sqrt


class TestBasicOperations:
    """Test basic arithmetic operations"""

    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6


class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""

    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")

    def test_multiply_numbers(self):
        """Test multiplication of numbers."""
        assert multiply(2, 3) == 6
        assert multiply(5, 4) == 20
        assert multiply(-2, 3) == -6

    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

    def test_divide_numbers(self):
        """Test division of valid numbers."""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5
        assert divide(7, 2) == 3.5

    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide"):
            divide(10, 0)


# TODO: Students will add TestMultiplyDivide class


class TestPower:
    """Test power function."""

    def test_power_numbers(self):
        assert power(2, 3) == 8
        assert power(5, 2) == 25
        assert power(2, 0) == 1

    def test_power_invalid_input(self):
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power("2", 3)


class TestSquareRoot:
    """Test square root function."""

    def test_sqrt_numbers(self):
        assert sqrt(25) == 5.0
        assert sqrt(81) == 9.0
        assert sqrt(0) == 0.0

    def test_sqrt_invalid_input(self):
        with pytest.raises(TypeError, match="Argument must be a number"):
            sqrt("25")

    def test_sqrt_negative_number(self):
        with pytest.raises(
            ValueError,
            match="Cannot calculate square root of a negative number",
        ):
            sqrt(-4)
