import os
import boto3
import psycopg2
import pandas as pd
from io import StringIO
from dotenv import load_dotenv

load_dotenv()
PG_HOST = os.getenv("PG_HOST")
PG_USER = os.getenv("PG_USER")
PG_PASSWD = os.getenv("PG_PASSWD")
PG_DB = os.getenv("PG_DB")

S3_BUCKET = os.getenv("S3_BUCKET")

def export_postgres():
    try:
        conn = psycopg2.connect(
            host=PG_HOST,
            database=PG_DB,
            user=PG_USER,
            password=PG_PASSWD
        )
        print("Connected to the database")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
    
    query_pets = "SELECT * FROM pet;"
    df_pets = pd.read_sql_query(query_pets, conn)
    print("Data fetched from pet")

    query_vaccine = "SELECT * FROM vaccine;"
    df_vaccine = pd.read_sql_query(query_vaccine, conn)
    print("Data fetched from vaccine")

    query_adoption_center = "SELECT * FROM adoption_center;"
    df_adoption_center = pd.read_sql_query(query_adoption_center, conn)
    print("Data fetched from adoption_center")

    query_adoption_status = "SELECT * FROM adoption_status;"
    df_adoption_status = pd.read_sql_query(query_adoption_status, conn)
    print("Data fetched from adoption_status")

    csv_buffer_pets = StringIO()
    df_pets.to_csv(csv_buffer_pets, index=False)

    csv_buffer_vaccine = StringIO()
    df_vaccine.to_csv(csv_buffer_vaccine, index=False)
    
    csv_buffer_adoption_center = StringIO()
    df_adoption_center.to_csv(csv_buffer_adoption_center, index=False)
    
    csv_buffer_adoption_status = StringIO()
    df_adoption_status.to_csv(csv_buffer_adoption_status, index=False)

    s3=boto3.client('s3')
    
    s3.put_object(Bucket=S3_BUCKET, Key='pets/pg_pets.csv', Body=csv_buffer_pets.getvalue())
    print("pets.csv uploaded to S3")

    s3.put_object(Bucket=S3_BUCKET, Key='vaccines/pg_vaccine.csv', Body=csv_buffer_vaccine.getvalue())
    print("vaccine.csv uploaded to S3") 

    s3.put_object(Bucket=S3_BUCKET, Key='adoption_centers/pg_adoption_center.csv', Body=csv_buffer_adoption_center.getvalue())
    print("adoption_center.csv uploaded to S3")

    s3.put_object(Bucket=S3_BUCKET, Key='adoption_status/pg_adoption_status.csv', Body=csv_buffer_adoption_status.getvalue())
    print("adoption_status.csv uploaded to S3")

    conn.close()
    print("All tables were exported to S3!")