"""This is a test file for my calculator program"""

from calculator import add, subtract  # Import the required functions

def test_addition():
    """Test that addition function works"""  
    assert add(2, 2) == 4  # ✅ Fixed indentation

def test_subtraction():
    """Test that subtraction function works"""  
    assert subtract(2, 2) == 0  # ✅ Correct function name
