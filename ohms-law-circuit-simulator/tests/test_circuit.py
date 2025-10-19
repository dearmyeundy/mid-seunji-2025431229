import pytest
from app.simulations.circuit import Circuit
from app.simulations.solver import calculate_current, calculate_resistance

def test_circuit_series():
    circuit = Circuit()
    circuit.add_resistor(10)  # 10 ohms
    circuit.add_resistor(20)  # 20 ohms
    circuit.set_voltage(30)    # 30 volts
    assert circuit.calculate_total_resistance() == 30  # Series: R_total = R1 + R2
    assert calculate_current(circuit.voltage, circuit.calculate_total_resistance()) == 1  # I = V / R_total

def test_circuit_parallel():
    circuit = Circuit()
    circuit.add_resistor(10)  # 10 ohms
    circuit.add_resistor(20)  # 20 ohms
    circuit.set_voltage(30)    # 30 volts
    assert circuit.calculate_total_resistance() == 6.0  # Parallel: 1/R_total = 1/R1 + 1/R2
    assert calculate_current(circuit.voltage, circuit.calculate_total_resistance()) == 5  # I = V / R_total

def test_calculate_current():
    voltage = 12
    resistance = 4
    assert calculate_current(voltage, resistance) == 3  # I = V / R

def test_calculate_resistance():
    voltage = 12
    current = 3
    assert calculate_resistance(voltage, current) == 4  # R = V / I

def test_invalid_resistor_value():
    circuit = Circuit()
    with pytest.raises(ValueError):
        circuit.add_resistor(-5)  # Negative resistance should raise an error

def test_no_resistors():
    circuit = Circuit()
    circuit.set_voltage(10)
    assert circuit.calculate_total_resistance() == 0  # No resistors should return 0 resistance
    assert calculate_current(circuit.voltage, circuit.calculate_total_resistance()) == 0  # No current should flow