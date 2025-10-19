def calculate_voltage(current, resistance):
    return current * resistance

def calculate_current(voltage, resistance):
    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")
    return voltage / resistance

def calculate_resistance(voltage, current):
    if current == 0:
        raise ValueError("Current cannot be zero.")
    return voltage / current

def validate_inputs(value):
    if value < 0:
        raise ValueError("Input values must be non-negative.")