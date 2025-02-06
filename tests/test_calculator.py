"""This is a test file for my calculator program""" 
from calculator import add  
'''My Calculator Test'''
from calculator import add, subtract

def test_addition():
    """The is a test of the addition function"""
    '''Test that addition function works '''    
assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0
    
