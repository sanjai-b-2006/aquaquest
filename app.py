import streamlit as st
import requests

# User provides the public JSON file URL
data_url = st.text_input("Enter the public JSON URL:", "https://example.com/data.json")

st.title("ESP32 Sensor Dashboard")

if st.button("Fetch Latest Data") or True:
    try:
        response = requests.get(data_url)
        data = response.json()
        ph = data.get("ph")
        distance = data.get("distance")
        st.metric("pH Value", ph if ph is not None else "No data")
        st.metric("Distance (cm)", distance if distance is not None else "No data")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
