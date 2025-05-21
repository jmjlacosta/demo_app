import streamlit as st

# Sidebar Overview
st.sidebar.title("Healthcare Demo App")
st.sidebar.markdown("Explore the capabilities of Streamlit apps on Health Universe.")

# Optional logo prompt
if st.sidebar.checkbox("Include logo (logo.png must be present)"):
    st.sidebar.image("logo.png", use_column_width=True)

# Header Section
st.title("🏥 Health Universe Streamlit Demo")
st.markdown("""
This is a demonstration Streamlit app built for the Health Universe platform.
Explore how to build and structure healthcare tools for deployment.
""")

# Disclaimer
with st.expander("Disclaimer"):
    st.markdown("""
    This app is for demonstration purposes only. No real patient data is used or shown.
    """)

# Sample UI Components
st.header("Interactive Widgets")
st.markdown("Try interacting with the widgets below to simulate healthcare app behavior.")

# Widgets
age = st.slider("Select Age", 0, 100, 50)
gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])
symptom = st.text_input("Enter a symptom")

# Simulated output
with st.expander("Simulated Response"):
    st.write(f"You selected Age: {age}, Gender: {gender}, Symptom: {symptom}")
    st.info("This is a placeholder output simulating diagnostic feedback.")

# Style support
with st.expander("Optional Style Support"):
    st.code("""Add a 'style.css' file to customize the look of your app.""")

# Footer
st.markdown("---")
st.markdown("Built for Health Universe • May 2025")
