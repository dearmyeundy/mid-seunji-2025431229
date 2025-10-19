from streamlit import st
import json
from app.components.widgets import voltage_slider, resistance_slider, circuit_type_selector
from app.simulations.circuit import Circuit

def main():
    st.title("Circuit Simulator")
    
    # Load sample circuits
    with open('app/data/sample_circuits.json') as f:
        sample_circuits = json.load(f)

    # Circuit configuration
    circuit_type = circuit_type_selector()
    voltage = voltage_slider()
    resistance = resistance_slider()

    # Create circuit based on user input
    circuit = Circuit(voltage, resistance, circuit_type)

    # Simulate circuit
    current = circuit.simulate()

    # Display results
    st.subheader("Simulation Results")
    st.write(f"Voltage: {voltage} V")
    st.write(f"Resistance: {resistance} Ω")
    st.write(f"Current: {current} A")

    # Display sample circuits
    st.subheader("Sample Circuits")
    for sample in sample_circuits:
        st.write(f"Circuit: {sample['name']}")
        st.write(f"Voltage: {sample['voltage']} V")
        st.write(f"Resistance: {sample['resistance']} Ω")
        st.write(f"Current: {sample['current']} A")
        st.write("---")

if __name__ == "__main__":
    main()