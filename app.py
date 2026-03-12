import streamlit as st
import requests

# User provides the public JSON file URL
data_url = st.text_input("Enter the public JSON URL:", "https://example.com/data.json")

st.title("ESP32 Sensor Dashboard")

if st.button("Fetch Latest Data") or True:
    try:
        response = requests.get(data_url)
        data = response.json()
        rf_message = data.get("rf_message", "")
        distance = None
        ph = None
        if rf_message:
            # Example: "1199.79cm,PH:4.66"
            parts = rf_message.split(",")
            if len(parts) == 2:
                distance_str = parts[0].replace("cm", "").strip()
                ph_str = parts[1].replace("PH:", "").strip()
                try:
                    distance = float(distance_str)
                except ValueError:
                    distance = None
                try:
                    ph = float(ph_str)
                except ValueError:
                    ph = None
        st.metric("pH Value", ph if ph is not None else "No data")
        st.metric("Distance (cm)", distance if distance is not None else "No data")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
