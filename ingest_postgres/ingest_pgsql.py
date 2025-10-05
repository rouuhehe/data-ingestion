import os
import csv
import boto3
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pandas as pd

load_dotenv()

S3_BUCKET = os.getenv("S3_BUCKET")
s3 = boto3.client('s3')

DB_URL = os.getenv("POSTGRES_URL") 
engine = create_engine(DB_URL)

tables = ["pet", "adoption_status", "vaccines", "adoption_centers"]

for table in tables:
    with engine.connect() as conn:
        df = pd.read_sql(text(f"SELECT * FROM {table}"), conn)

    csv_file = f"{table}.csv"
    df.to_csv(csv_file, index=False)

    s3.upload_file(csv_file, S3_BUCKET, f'postgres/{csv_file}')
    print(f"{table} table was exported to S3")

print("Postgres export completed")
