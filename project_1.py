import streamlit as st
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# STEP 1: Load the CSV or Excel file
file_path_excel = "C:\\Users\\BARANI\\Downloads\\traffic_stops.xlsx"   # For Excel


df = pd.read_excel(file_path_excel)

# STEP 2: Define PostgreSQL connection string
username = 'bkguru90'
password = 'bYrCL6htcluV55EeU2uBc7MfdVbM3jR8'
host = 'dpg-d0kn73vfte5s738r4uvg-a.singapore-postgres.render.com'        # e.g., localhost or remote server
port = '5432'
database = 'barani_db'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

st.write("Hello world!")
df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.table(df)

agree = st.checkbox("Vehicle Number")

if agree:
    st.write("You selected:", agree)
    vehicle_no = st.text_input("Please Enter the Vehicle Number: ")
    Qurey3=f"SELECT * FROM traffic_stops WHERE vehicle_number = '{vehicle_no}'"
    new_traffic3_df=pd.read_sql(Qurey3,engine)
    st.dataframe(new_traffic3_df)

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
        st.write(new_traffic3_df)
    
        st.write(column)
st.write("Outside the form")
    