import streamlit as st
import pytz
from datetime import datetime
import time

# Set page config
st.set_page_config(page_title="🌍 Time Zone Tracker", page_icon="🕰️", layout="centered")

# Title and description
st.title("🌍 Time Zone Tracker")
st.markdown("Effortlessly track time across different time zones with this intuitive tracker.")

# Sidebar for settings
st.sidebar.header("Settings")
timezones = pytz.all_timezones

# Ensure Pakistan timezone is included if missing
if "Asia/Karachi" not in timezones:
    timezones.append("Asia/Karachi")

selected_timezones = st.sidebar.multiselect("Select Time Zones", timezones, default=["UTC", "America/New_York", "Asia/Kolkata", "Asia/Karachi"])

# Function to get current time
def get_time(tz):
    timezone = pytz.timezone(tz)
    return datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")

# Display the selected time zones with better UI
st.subheader("🕒 Current Time in Selected Time Zones")

col1, col2 = st.columns(2)

with col1:
    for i, tz in enumerate(selected_timezones[:len(selected_timezones)//2]):
        st.info(f"**{tz}:** {get_time(tz)}")

with col2:
    for i, tz in enumerate(selected_timezones[len(selected_timezones)//2:]):
        st.success(f"**{tz}:** {get_time(tz)}")

# Auto-refresh using Streamlit's session state
if "last_refresh" not in st.session_state:
    st.session_state["last_refresh"] = datetime.now()

def refresh():
    st.session_state["last_refresh"] = datetime.now()

st.button("🔄 Refresh Time", on_click=refresh)

st.markdown("\n*Click the refresh button to update the time.*")
