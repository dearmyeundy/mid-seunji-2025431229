import streamlit as st

def main():
    st.title("Ohm's Law and Circuit Simulator")
    st.sidebar.title("Navigation")
    
    pages = {
        "Ohm's Law": "pages/ohms_law.py",
        "Circuit Simulator": "pages/circuit_simulator.py"
    }
    
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    if selection == "Ohm's Law":
        st.markdown("### Ohm's Law")
        st.write("Visualize the relationship between voltage, current, and resistance.")
        # Import and run the Ohm's Law page
        exec(open(pages[selection]).read())
    elif selection == "Circuit Simulator":
        st.markdown("### Circuit Simulator")
        st.write("Create and simulate electrical circuits.")
        # Import and run the Circuit Simulator page
        exec(open(pages[selection]).read())

if __name__ == "__main__":
    main()