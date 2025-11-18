import pytest
from src.pricing import apply_discount

def test_apply_discount_regression():
    result = apply_discount(100.0, 10)
    
    assert result == 90.0, f"Expected 90.0 but got {result}"

def test_apply_discount_regression_25_percent():
    result = apply_discount(200.0, 25)
    assert result == 150.0, f"Expected 150.0 but got {result}"

def test_apply_discount_regression_50_percent():
    result = apply_discount(80.0, 50)
    assert result == 40.0, f"Expected 40.0 but got {result}"
