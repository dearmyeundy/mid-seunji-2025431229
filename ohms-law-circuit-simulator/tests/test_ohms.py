import pytest
from app.simulations.solver import calculate_current, calculate_resistance

def test_calculate_current():
    # Test with valid inputs
    voltage = 10  # Volts
    resistance = 5  # Ohms
    expected_current = 2  # Amperes
    assert calculate_current(voltage, resistance) == expected_current

    # Test with zero resistance (should handle division by zero)
    resistance = 0
    with pytest.raises(ZeroDivisionError):
        calculate_current(voltage, resistance)

def test_calculate_resistance():
    # Test with valid inputs
    voltage = 10  # Volts
    current = 2  # Amperes
    expected_resistance = 5  # Ohms
    assert calculate_resistance(voltage, current) == expected_resistance

    # Test with zero current (should handle division by zero)
    current = 0
    with pytest.raises(ZeroDivisionError):
        calculate_resistance(voltage, current)