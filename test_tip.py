import pytest

from tip import *

def test_pytest():
    assert True == True

# Create your tests below

# Test 1 - check that the function returns the correct value for a 10% tip on a value of 10
def test_10_percent():
assert calculate_tip(10,10) == 1

# Test 2 - check that the function throws a ValueError error for negative values. Test with -200 (negative 200) as the amount.


# Test 3 - check that the function throws a TypeError error for string input. Use the string ‘ten’ as input for the tip.

