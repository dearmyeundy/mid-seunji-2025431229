class Circuit:
    def __init__(self, voltage=0, resistance=0):
        self.voltage = voltage
        self.resistance = resistance
        self.current = self.calculate_current()

    def calculate_current(self):
        if self.resistance == 0:
            return float('inf')  # Infinite current if resistance is zero
        return self.voltage / self.resistance

    def update_parameters(self, voltage, resistance):
        self.voltage = voltage
        self.resistance = resistance
        self.current = self.calculate_current()

    def get_circuit_info(self):
        return {
            "Voltage (V)": self.voltage,
            "Resistance (Ω)": self.resistance,
            "Current (A)": self.current
        }

def simulate_series_circuit(circuits):
    total_voltage = sum(circuit.voltage for circuit in circuits)
    total_resistance = sum(circuit.resistance for circuit in circuits)
    total_current = total_voltage / total_resistance if total_resistance != 0 else float('inf')
    return total_voltage, total_resistance, total_current

def simulate_parallel_circuit(circuits):
    total_resistance = sum(1 / circuit.resistance for circuit in circuits if circuit.resistance != 0)
    total_resistance = 1 / total_resistance if total_resistance != 0 else float('inf')
    total_voltage = circuits[0].voltage if circuits else 0
    total_current = total_voltage / total_resistance if total_resistance != 0 else float('inf')
    return total_voltage, total_resistance, total_current