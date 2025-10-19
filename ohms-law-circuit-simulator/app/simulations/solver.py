def calculate_current(voltage, resistance):
    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")
    return voltage / resistance

def calculate_resistance(voltage, current):
    if current == 0:
        raise ValueError("Current cannot be zero.")
    return voltage / current

def calculate_voltage(current, resistance):
    return current * resistance

def solve_circuit(voltage=None, current=None, resistance=None):
    if voltage is not None and current is not None:
        resistance = calculate_resistance(voltage, current)
        return {"voltage": voltage, "current": current, "resistance": resistance}
    elif voltage is not None and resistance is not None:
        current = calculate_current(voltage, resistance)
        return {"voltage": voltage, "current": current, "resistance": resistance}
    elif current is not None and resistance is not None:
        voltage = calculate_voltage(current, resistance)
        return {"voltage": voltage, "current": current, "resistance": resistance}
    else:
        raise ValueError("At least two parameters (voltage, current, resistance) must be provided.")