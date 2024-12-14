import streamlit as st
import pandas as pd
from datetime import datetime

# Academic Calendar Data
data = {
    "Date": [
        "13 Dec", "14 Dec", "15 Dec", "16 Dec", "17 Dec", "18 Dec", "19 Dec", "20 Dec", "21 Dec",
        "22 Dec", "23 Dec", "24 Dec", "25 Dec", "26 Dec", "27 Dec", "28 Dec", "29 Dec", "30 Dec", "31 Dec", "1 Jan",
        "2 Jan", "3 Jan", "4 Jan", "5 Jan", "6 Jan", "7 Jan", "8 Jan", "9 Jan", "10 Jan", "11 Jan", "12 Jan",
        "13 Jan", "14 Jan", "15 Jan", "16 Jan", "17 Jan", "18 Jan", "19 Jan", "20 Jan", "21 Jan", "22 Jan",
        "23 Jan", "24 Jan", "25 Jan", "26 Jan", "27 Jan", "28 Jan", "29 Jan", "30 Jan", "31 Jan",
        "1 Feb", "2 Feb", "3 Feb", "4 Feb", "5 Feb", "6 Feb", "7 Feb", "8 Feb", "9 Feb", "10 Feb", "11 Feb",
        "12 Feb", "13 Feb", "14 Feb", "15 Feb", "16 Feb", "17 Feb", "18 Feb", "19 Feb", "20 Feb", "21 Feb",
        "22 Feb", "23 Feb", "24 Feb", "25 Feb", "26 Feb", "27 Feb", "28 Feb", "1 Mar", "2 Mar", "3 Mar", "4 Mar",
        "5 Mar", "6 Mar", "7 Mar", "8 Mar", "9 Mar", "10 Mar", "11 Mar", "12 Mar", "13 Mar", "14 Mar", "15 Mar",
        "16 Mar", "17 Mar", "18 Mar", "19 Mar", "20 Mar", "21 Mar", "22 Mar", "23 Mar", "24 Mar", "25 Mar",
        "26 Mar", "27 Mar", "28 Mar", "29 Mar", "30 Mar", "31 Mar", "1 Apr", "2 Apr", "3 Apr", "4 Apr", "5 Apr",
        "6 Apr", "7 Apr", "8 Apr", "9 Apr", "10 Apr", "11 Apr", "12 Apr", "13 Apr", "14 Apr", "15 Apr", "16 Apr",
        "17 Apr"
    ],
    "Details": [
        "First Instructional Day", "Instructional Day (Monday Day Order)", "Instructional Day", "Instructional Day",
        "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day (Tuesday Day Order)",
        "Holiday (Winter Vacation)", "Holiday (Winter Vacation)", "Holiday (Winter Vacation)", "Holiday (Winter Vacation)",
        "Holiday (Winter Vacation)", "Holiday (Winter Vacation)", "Holiday (Winter Vacation)", "Holiday (Winter Vacation)",
        "Holiday (Winter Vacation)", "Holiday (Winter Vacation)", "Holiday (Winter Vacation)",
        "Instructional Day", "Instructional Day", "Instructional Day (Wednesday Day Order)", "Instructional Day",
        "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day",
        "Instructional Day (Thursday Day Order)", "Instructional Day", "Instructional Day", "Holiday (Pongal Holidays)",
        "Holiday (Pongal Holidays)", "Instructional Day", "Instructional Day", "Instructional Day (Friday Day Order)",
        "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day",
        "Instructional Day", "Instructional Day", "Holiday (Republic Day)", "CAT - I (Exam Day)", "CAT - I (Exam Day)",
        "CAT - I (Exam Day)", "CAT - I (Exam Day)", "CAT - I (Exam Day)", "CAT - I (Exam Day)", "Instructional Day",
        "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day",
        "Instructional Day", "Holiday (Thai Poosam)", "Instructional Day", "Instructional Day", "Instructional Day",
        "Instructional Day", "Instructional Day (Monday Day Order)", "Instructional Day", "Instructional Day",
        "Instructional Day", "No Instructional Day (Riviera 2025)", "No Instructional Day (Riviera 2025)",
        "No Instructional Day (Riviera 2025)", "No Instructional Day (Riviera 2025)", "Instructional Day",
        "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day (Tuesday Day Order)",
        "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day",
        "Instructional Day", "Instructional Day (Wednesday Day Order)", "Instructional Day", "Instructional Day",
        "Instructional Day", "Instructional Day", "Instructional Day", "Holiday (Holi)", "CAT - II (Exam Day)",
        "CAT - II (Exam Day)", "CAT - II (Exam Day)", "CAT - II (Exam Day)", "CAT - II (Exam Day)", "CAT - II (Exam Day)",
        "CAT - II (Exam Day)", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day",
        "Instructional Day", "Instructional Day", "Instructional Day (Monday Day Order)", "No Instructional Day (Telugu New Year)",
        "Holiday (Ramzan)", "Instructional Day", "Instructional Day", "Instructional Day", "Instructional Day",
        "Instructional Day (Last for lab)", "Instructional Day", "Instructional Day", "Instructional Day",
        "Instructional Day", "Instructional Day", "Instructional Day (Tuesday Day Order)", "Instructional Day",
        "Holiday (Tamil New Year)", "Instructional Day", "Instructional Day", "Instructional Day (Last for theory)"
    ]
}

# Convert to DataFrame
calendar_df = pd.DataFrame(data)
calendar_df["Date"] = calendar_df["Date"] + " 2024"
calendar_df["Date"] = pd.to_datetime(calendar_df["Date"], format="%d %b %Y")
calendar_df["Month"] = calendar_df["Date"].dt.strftime("%B")
calendar_df["Day_Type"] = calendar_df["Details"].apply(
    lambda x: "Instructional Day" if "Instructional" in x else "Non-Instructional Day"
)

# Streamlit App
st.title("Academic Calendar Viewer")

# Sidebar Options
selected_month = st.sidebar.selectbox("Select a Month", sorted(calendar_df["Month"].unique()))
selected_day_type = st.sidebar.selectbox(
    "Select Day Type", ["All", "Instructional Day", "Non-Instructional Day"]
)

# Filter Data
filtered_df = calendar_df[calendar_df["Month"] == selected_month]
if selected_day_type != "All":
    filtered_df = filtered_df[filtered_df["Day_Type"] == selected_day_type]

# Display Results
st.header(f"Academic Calendar for {selected_month}")
st.table(filtered_df[["Date", "Details"]])

# Button to Display Totals
if st.button("Show Summary"):
    total_instructional = len(calendar_df[(calendar_df["Month"] == selected_month) & (calendar_df["Day_Type"] == "Instructional Day")])
    total_non_instructional = len(calendar_df[(calendar_df["Month"] == selected_month) & (calendar_df["Day_Type"] == "Non-Instructional Day")])

    st.write(f"### Summary for {selected_month}")
    st.write(f"- Total Instructional Days: {total_instructional}")
    st.write(f"- Total Non-Instructional Days: {total_non_instructional}")
