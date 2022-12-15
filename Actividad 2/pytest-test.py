import pytest
from Script import suma, resta, multiplicar, division,exponente

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-2, -3) == -5
    assert suma(0, 0) == 0

def test_resta():
    assert resta(2, 3) == -1
    assert resta(-2, -3) == 1
    assert resta(0, 0) == 0

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-2, -3) == 6
    assert multiplicar(0, 0) == 0

def test_division():
    assert division(2, 3) == 2/3
    assert division(-2, -3) == 2/3
    with pytest.raises(ValueError):
        division(2, 0)
def test_exponente():
    assert exponente(2,3)==2**3
    assert exponente(-2,-3) ==-2**-3
    assert exponente(0,0) == 1
