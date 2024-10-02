'''My Calculator Test'''
from calculator.operations import add, multiply, subtract, divide

def test_addition():
    """Addition Test"""    
    assert add(2,2) == 4

def test_subtraction():
    """Subtraction Test"""    
    assert subtract(2,2) == 0

def test_multiplication():
    """Multiplication Test"""
    assert multiply(2,2) == 4

def test_division():
    """Division Test"""
    assert divide(2,2) == 1
