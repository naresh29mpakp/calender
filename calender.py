import streamlit as st
import pandas as pd

# Define the Date and Details lists
dates = [
    "13 Dec", "14 Dec", "15 Dec", "16 Dec", "17 Dec", "18 Dec", "19 Dec", "20 Dec", "21 Dec", "22 Dec",
    "23 Dec", "24 Dec", "25 Dec", "26 Dec", "27 Dec", "28 Dec", "29 Dec", "30 Dec", "31 Dec", "1 Jan",
    "2 Jan", "3 Jan", "4 Jan", "5 Jan", "6 Jan", "7 Jan", "8 Jan", "9 Jan", "10 Jan", "11 Jan", "12 Jan", 
    "13 Jan", "14 Jan", "15 Jan", "16 Jan", "17 Jan", "18 Jan", "19 Jan", "20 Jan", "21 Jan", "22 Jan", 
    "23 Jan", "24 Jan", "25 Jan", "26 Jan", "27 Jan", "28 Jan", "29 Jan", "30 Jan", "31 Jan", "1 Feb",
    "2 Feb", "3 Feb", "4 Feb", "5 Feb", "6 Feb", "7 Feb", "8 Feb", "9 Feb", "10 Feb", "11 Feb", "12 Feb",
    "13 Feb", "14 Feb", "15 Feb", "16 Feb", "17 Feb", "18 Feb", "19 Feb", "20 Feb", "21 Feb", "22 Feb",
    "23 Feb", "24 Feb", "25 Feb", "26 Feb", "27 Feb", "28 Feb", "1 Mar", "2 Mar", "3 Mar", "4 Mar", "5 Mar",
    "6 Mar", "7 Mar", "8 Mar", "9 Mar", "10 Mar", "11 Mar", "12 Mar", "13 Mar", "14 Mar", "15 Mar", "16 Mar",
    "17 Mar", "18 Mar", "19 Mar", "20 Mar", "21 Mar", "22 Mar", "23 Mar", "24 Mar", "25 Mar", "26 Mar", 
    "27 Mar", "28 Mar", "29 Mar", "30 Mar", "31 Mar", "1 Apr", "2 Apr", "3 Apr", "4 Apr", "5 Apr", "6 Apr", 
    "7 Apr", "8 Apr", "9 Apr", "10 Apr", "11 Apr", "12 Apr", "13 Apr", "14 Apr", "15 Apr", "16 Apr", "17 Apr"
]

details = [
    "First Instructional Day", "Instructional Day (Monday Day Order)", "Instructional Day", "Instructional Day",
    "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day (Tuesday Day Order)",
    "Holiday (Winter Vacation)", "Holiday (Winter Vacation)", "Holiday (Winter Vacation)", "Holiday (Winter Vacation)",
    "Holiday (Winter Vacation)", "Holiday (Winter Vacation)", "Holiday (Winter Vacation)", "Holiday (Winter Vacation)",
    "Holiday (Winter Vacation)", "Holiday (Winter Vacation)", "Holiday (Winter Vacation)", "Instructional Day",
    "Instructional Day", "Instructional Day", "Instructional Day (Wednesday Day Order)", "Instructional Day", "Instructional Day",
    "Instructional Day", "Instructional Day", "Holiday (Pongal Holidays)", "Holiday (Pongal Holidays)", "Instructional Day",
    "Instructional Day", "Instructional Day (Friday Day Order)", "Instructional Day", "Instructional Day", "Instructional Day",
    "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day",
    "Instructional Day (Tuesday Day Order)", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day",
    "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day",
    "Instructional Day", "Holiday (Tamil New Year)", "Instructional Day", "Instructional Day", "Instructional Day (Last for theory)",
    "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day",
    "Instructional Day", "Holiday (Ramzan)", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day",
    "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day",
    "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day",
    "Instructional Day", "Holiday (Tamil New Year)", "Instructional Day", "Instructional Day", "Instructional Day (Last for theory)"
]

# Ensure both lists have the same length by truncating the longer one
min_length = min(len(dates), len(details))
dates = dates[:min_length]
details = details[:min_length]

# Create the pandas DataFrame
schedule_df = pd.DataFrame({
    "Date": dates,
    "Details": details
})

# Display the table in Streamlit
st.title("Academic Schedule")
st.write(schedule_df)
