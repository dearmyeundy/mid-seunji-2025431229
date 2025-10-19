from streamlit import slider, button, selectbox, text_input

def voltage_slider():
    return slider("Voltage (V)", min_value=0.0, max_value=100.0, value=10.0, step=0.1)

def resistance_slider():
    return slider("Resistance (Ω)", min_value=1.0, max_value=100.0, value=10.0, step=0.1)

def current_display(current):
    return text_input("Current (A)", value=str(current), disabled=True)

def circuit_configuration_selector():
    return selectbox("Select Circuit Configuration", options=["Series", "Parallel"])

def simulate_button():
    return button("Simulate Circuit")