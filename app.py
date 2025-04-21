import streamlit as st
from unit_converter import convert_units

st.set_page_config(page_title="Unit Converter", page_icon="🔄")
st.title("🔄 Unit Converter")

value = st.number_input("Enter value to convert:")
from_unit = st.selectbox("From Unit:", ['kilometers', 'miles', 'meters', 'feet', 'celsius', 'fahrenheit'])
to_unit = st.selectbox("To Unit:", ['kilometers', 'miles', 'meters', 'feet', 'celsius', 'fahrenheit'])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"Converted Value: {result}")

