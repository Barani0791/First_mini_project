import pandas as pd
from sqlalchemy import create_engine

# STEP 1: Load the CSV or Excel file
# For CSV
file_path_excel = "C:\\Users\\BARANI\\Downloads\\traffic_stops.xlsx"    # For Excel

# Uncomment the one you want to use
# df = pd.read_csv(file_path_csv)
df = pd.read_excel(file_path_excel)

# STEP 2: Define PostgreSQL connection string
# Replace the values below with your credentials
username = 'bkguru90'
password = 'bYrCL6htcluV55EeU2uBc7MfdVbM3jR8'
host = 'dpg-d0kn73vfte5s738r4uvg-a.singapore-postgres.render.com'        # e.g., localhost or remote server
port = '5432'
database = 'barani_db'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

# STEP 3: Upload to PostgreSQL table
table_name = 'traffic_stops'  # Choose your table name
df.to_sql(table_name, engine, if_exists='replace', index=False)

print(f"✅ Data successfully imported into '{table_name}' table.")