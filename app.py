import streamlit as st

# Custom Styling
st.markdown(
    """
    <style>
        .main { background-color: #f5f5f5; padding: 20px; border-radius: 10px; }
        .title { text-align: center; color: #4CAF50; font-size: 32px; font-weight: bold; }
        .stButton>button { background-color: #4CAF50; color: white; font-size: 18px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown("<h1 class='title'>🔄 Advanced Universal Unit Converter</h1>", unsafe_allow_html=True)

# Sidebar for selection
st.sidebar.header("🔧 Settings")
conversion_types = ["Length", "Weight", "Volume", "Speed", "Time", "Energy"]
conversion_choice = st.sidebar.radio("**Choose Conversion Type:**", conversion_types)

# Conversion Factors
conversion_factors = {
    "Length": {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084},
    "Weight": {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462},
    "Volume": {"Liters": 1, "Milliliters": 1000, "Gallons": 0.264172},
    "Speed": {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694},
    "Time": {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600},
    "Energy": {"Joules": 1, "Kilojoules": 0.001, "Calories": 0.239006}
}

# Select Units
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("Convert From:", list(conversion_factors[conversion_choice].keys()))
with col2:
    to_unit = st.selectbox("Convert To:", list(conversion_factors[conversion_choice].keys()))

# Input Value
value = st.number_input(f"Enter value in {from_unit}:", min_value=0.0, step=0.1, format="%.2f")

# Convert Button
if st.button("Convert 🔄"):
    result = value * (conversion_factors[conversion_choice][to_unit] / conversion_factors[conversion_choice][from_unit])
    st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")
