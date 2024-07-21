import streamlit as st
from datetime import datetime, timedelta

def get_on_off_days(start_date, num_days_on, num_days_off, year):
    on_off_days = []
    current_date = start_date
    while current_date.year == year:
        for _ in range(num_days_on):
            on_off_days.append((current_date, current_date.strftime("%A"), "On"))
            current_date += timedelta(days=1)
        for _ in range(num_days_off):
            on_off_days.append((current_date, current_date.strftime("%A"), "Off"))
            current_date += timedelta(days=1)
    return on_off_days

st.title("Work Schedule Generator")

start_date = st.date_input("Start Date", datetime(2024, 4, 8))
num_days_on = st.number_input("Number of Days On", min_value=1, step=1, value=4)
num_days_off = st.number_input("Number of Days Off", min_value=1, step=1, value=4)
year = start_date.year

if st.button("Generate Schedule"):
    on_off_days = get_on_off_days(start_date, num_days_on, num_days_off, year)
    st.write("### Work Schedule for", year)
    for date, day, status in on_off_days:
        st.write(f"- {date.strftime('%A, %d %B %Y')} - {day} - {status}")
