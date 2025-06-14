import streamlit as st
import pandas as pd
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

# STEP 3: Upload to PostgreSQL table
#table_name = 'traffic_stops'  # Choose your table name
#df.to_sql(table_name, engine, if_exists='replace', index=False)

#print(f"✅ Data successfully imported into '{table_name}' table.")

vehicle_no = st.text_input("Enter Vehicle Number: ")

Qurey3=f"SELECT * FROM traffic_stops WHERE vehicle_number = '{vehicle_no}'"
new_traffic3_df=pd.read_sql(Qurey3,engine)

st.dataframe(new_traffic3_df)