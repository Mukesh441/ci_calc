# Unit tests for the Python application
"""
Test cases for the calculator module.
"""

import pytest
from calculator.calc import add, subtract

def test_add():
    """Test the add function."""
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """Test the subtract function."""
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5
    assert subtract(5, 5) == 0


if __name__ == "__main__":
    pytest.main()

    # Final newline added here.
