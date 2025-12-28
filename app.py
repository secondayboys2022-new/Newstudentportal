import streamlit as st
import pandas as pd

import os

# Page setup
st.set_page_config(page_title="Student Data Finder", layout="centered")

# Custom CSS to make labels look like a professional form
st.markdown("""
    <style>
    .reportview-container { background: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    label { font-weight: bold; color: #4A4A4A; }
    </style>
    """, unsafe_allow_html=True)



@st.cache_data
def load_data():
    # 1. List all files in the current folder
    all_files = os.listdir(".")
    
    # 2. Find any file that ends with .xlsx
    excel_files = [f for f in all_files if f.endswith(".xlsx")]
    
    if not excel_files:
        st.error("❌ No Excel (.xlsx) file was found in your GitHub folder.")
        st.info(f"Files currently in your folder: {all_files}")
        st.stop()
    
    # 3. Pick the first excel file found
    target_file = excel_files[0]
    st.sidebar.success(f"Connected to: {target_file}")
    
    return pd.read_excel(target_file)

# Call the function
df = load_data()

st.title("🔍 Student Record Search")
st.write("Enter a National ID below to view student details.")

# --- FORM SECTION ---
with st.container():
    # Text Field for National ID
    target_id = st.text_input("Enter Student National ID:", placeholder="Enter ID here...")
    
    search_button = st.button("Search Student")

    if target_id or search_button:
        try:
            df = load_data()
            # Search logic
            result = df[df['National_ID'].astype(str) == str(target_id)]

            if not result.empty:
                st.success("Record Found!")
                student = result.iloc[0]

                # Displaying info in 4 distinct Labels/Boxes
                col1, col2 = st.columns(2)

                with col1:
                    st.text_input("Full Name", value=student['Name'], disabled=True)
                    st.text_input("Email Address", value=student['Email'], disabled=True)

                with col2:
                    st.text_input("Class/Grade", value=student['Class'], disabled=True)
                    # For password, we use a password type input so it stays hidden unless clicked
                    st.text_input("Student Password", value=student['Password'], type="password", disabled=True)
                
                st.info("Note: Fields are locked. Contact Admin to change data.")
                
            else:
                st.error("No student found with that National ID.")
        except Exception as e:
            st.error(f"Please ensure 'students.xlsx' is uploaded. Error: {e}")

