import streamlit as st

st.set_page_config(page_title="Unit Converter")

st.title(" Unit Converter")

st.write("Enter  numbers and choose an operation:")


num1 = st.number_input("Enter number", value=0.0)

operation = st.selectbox(
    "Select operation",
    ("Liters → Milliliters", "Liters → Gallons", "Hours → Minutes", "Seconds → Minutes","Celsius → Fahrenheit","Celsius → Kelvin")
)


if st.button("Calculate"):
    if operation == "Liters → Milliliters":
        result = num1*1000
        st.success(f"ml: {result}")

elif operation == "Liters → Gallons":
        result = num1/3.78541
        st.success(f"gal: {result}")

elif operation == "Hours → Minutes":
        result = num1*60
        st.success(f"min: {result}")

elif operation == "Seconds → Minutes":
         result = num1/60
         st.success(f"min: {result}")

elif operation == "Celsius → Fahrenheit":
         result = (num1*9/5)+32
         st.success(f"F: {result}")

else:
         result = num1+273.15
         st.success(f"F: {result}")




    