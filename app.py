import streamlit as st
import pandas as pd

# Load the excel file
df = pd.read_excel("students.xlsx")

st.title("Student Information Portal")

# Search Input
search_id = st.text_input("Enter Student National ID:")

if search_id:
    # Filter the dataframe
    # Ensure the ID column is treated as a string for comparison
    result = df[df['National_ID'].astype(str) == search_id]

    if not result.empty:
        st.success("Student Found!")
        # Display the specific info
        st.write(f"**Name:** {result.iloc[0]['Name']}")
        st.write(f"**Email:** {result.iloc[0]['Email']}")
        st.write(f"**Password:** {result.iloc[0]['Password']}")
    else:
        st.error("No student found with that ID.")