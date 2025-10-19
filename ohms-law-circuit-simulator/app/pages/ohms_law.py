import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_current(voltage, resistance):
    if resistance == 0:
        return 0
    return voltage / resistance

def plot_vi_graph(voltage, current):
    plt.figure(figsize=(10, 5))
    plt.plot(voltage, current, marker='o')
    plt.title("Voltage vs Current (Ohm's Law)")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (I)")
    plt.grid()
    st.pyplot(plt)

def main():
    st.title("Ohm's Law Simulator")
    
    st.sidebar.header("Input Parameters")
    voltage = st.sidebar.slider("Voltage (V)", 0, 100, 10)
    resistance = st.sidebar.slider("Resistance (Ω)", 0, 100, 10)

    current = calculate_current(voltage, resistance)
    
    st.write(f"Calculated Current (I): {current:.2f} A")
    
    voltage_range = np.linspace(0, voltage, 100)
    current_values = calculate_current(voltage_range, resistance)
    
    plot_vi_graph(voltage_range, current_values)

if __name__ == "__main__":
    main()