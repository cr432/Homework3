'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    """Addition Test"""    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    """Subtraction Test"""    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    """Multiplication Test"""    
    assert Calculator.multiply(2,2) == 4

def test_divide():
    """Division Test"""    
    assert Calculator.divide(2,2) == 1
