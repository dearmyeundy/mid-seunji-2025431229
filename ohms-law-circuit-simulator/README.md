# Ohm's Law Circuit Simulator

This project is a web application built using Streamlit that allows users to explore Ohm's Law and simulate electrical circuits. The application provides an interactive interface for visualizing the relationship between voltage, current, and resistance, as well as creating and simulating various circuit configurations.

## Features

- **Ohm's Law Visualization**: Users can visualize the relationship between voltage (V), current (I), and resistance (R) through interactive elements and intuitive metaphors.
- **Circuit Simulator**: Create and simulate electrical circuits with options for series and parallel connections. Users can input different values for voltage and resistance to see how they affect the circuit.
- **Graphical Representation**: The application includes plotting capabilities to visualize current flow and V-I graphs, enhancing the understanding of circuit behavior.
- **Sample Circuits**: Predefined circuit configurations are available for demonstration purposes, allowing users to quickly see the application in action.

## Project Structure

```
ohms-law-circuit-simulator
├── app
│   ├── main.py                  # Entry point of the Streamlit application
│   ├── pages
│   │   ├── ohms_law.py          # Ohm's Law page implementation
│   │   └── circuit_simulator.py  # Circuit simulator page implementation
│   ├── components
│   │   ├── plotting.py           # Functions for plotting graphs
│   │   └── widgets.py            # Custom Streamlit widgets
│   ├── simulations
│   │   ├── circuit.py            # Logic for simulating electrical circuits
│   │   └── solver.py             # Functions for calculating circuit values
│   ├── utils
│   │   └── helpers.py            # Utility functions for data processing
│   └── data
│       └── sample_circuits.json  # Sample circuit configurations
├── tests
│   ├── test_ohms.py              # Unit tests for Ohm's Law functionalities
│   └── test_circuit.py           # Unit tests for circuit simulator functionalities
├── .gitignore                     # Files and directories to ignore by Git
├── requirements.txt               # Project dependencies
├── pyproject.toml                 # Project configuration
└── README.md                      # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ohms-law-circuit-simulator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run app/main.py
   ```

## Usage

Once the application is running, you can navigate between the Ohm's Law page and the Circuit Simulator page using the sidebar. Input values for voltage and resistance to see the results in real-time, and explore different circuit configurations to understand their behavior.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.