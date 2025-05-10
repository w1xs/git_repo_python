import pytest
def factorial(n):
    if not isinstance(n, int):
        raise ValueError("Факториал определен только для целых чисел")
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_factorial_positive():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

def test_factorial_negative_number():
    with pytest.raises(ValueError):
        factorial(-5)

def test_factorial_non_integer():
    with pytest.raises(ValueError):
        factorial(5.5)
    with pytest.raises(ValueError):
        factorial("5")
