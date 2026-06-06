
import streamlit as st

data = [
    {"Name": "Somchai", "Year": 1, "Weight": 68, "Height": 175, "BP": 118, "HR": 64},
    {"Name": "Somchai", "Year": 2, "Weight": 72, "Height": 175, "BP": 122, "HR": 68},
    {"Name": "Somchai", "Year": 3, "Weight": 78, "Height": 175, "BP": 129, "HR": 73},
    {"Name": "Somchai", "Year": 4, "Weight": 85, "Height": 175, "BP": 138, "HR": 81},
    {"Name": "Somchai", "Year": 5, "Weight": 93, "Height": 175, "BP": 148, "HR": 89},
    {"Name": "Somying", "Year": 1, "Weight": 99, "Height": 168, "BP": 156, "HR": 96},
    {"Name": "Somying", "Year": 2, "Weight": 95, "Height": 168, "BP": 148, "HR": 88},
    {"Name": "Somying", "Year": 3, "Weight": 86, "Height": 168, "BP": 136, "HR": 79},
    {"Name": "Somying", "Year": 4, "Weight": 77, "Height": 168, "BP": 124, "HR": 71},
    {"Name": "Somying", "Year": 5, "Weight": 71, "Height": 168, "BP": 118, "HR": 65},
]

st.line_chart(data, x="Year", y="Weight", color="Name")
st.bar_chart(data, x="Year", y="Weight", color="Name", stack=False)
st.scatter_chart(data, x="Year", y=None, color="Name", size="HR")