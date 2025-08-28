import pandas as pd
import pymysql
from sqlalchemy import create_engine
df = pd.read_csv('Customer_Data.csv')

# MySQL connection config
user = "****"
password = "********"
host = "localhost"
port = "3306"
database = "churn_db"

# Create connection
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

df.to_sql('stg_churn', con=engine, if_exists='replace', index=False)

print("Table uploaded successfully!")