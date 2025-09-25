import os
import boto3
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWD = os.getenv("MYSQL_PASSWD")
MYSQL_DB = os.getenv("MYSQL_DB")

S3_BUCKET = os.getenv("S3_BUCKET")

def export_mysql():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            database=MYSQL_DB,
            user=MYSQL_USER,
            password=MYSQL_PASSWD
        )
        print("Connected to the database")
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None
    
    query_users = "SELECT * FROM user;"
    df_users = pd.read_sql(query_users, conn)
    print("Data fetched from user")

    query_application = "SELECT * FROM application;"
    df_application = pd.read_sql(query_application, conn)
    print("Data fetched from adoption_center")

    query_adoption_history = "SELECT * FROM adoption_history;"
    df_adoption_history = pd.read_sql(query_adoption_history, conn)
    print("Data fetched from adoption_status")

    csv_buffer_users = df_users.to_csv(index=False)
    csv_buffer_application = df_application.to_csv(index=False)
    csv_buffer_adoption_history = df_adoption_history.to_csv(index=False)

    s3 = boto3.client('s3')
    
    s3.put_object(Bucket=S3_BUCKET, Key='users/mysql_users.csv', Body=csv_buffer_users)
    print("users.csv uploaded to S3")
    
    s3.put_object(Bucket=S3_BUCKET, Key='applications/mysql_vaccine.csv', Body=csv_buffer_application)
    print("applications.csv uploaded to S3")
    
    s3.put_object(Bucket=S3_BUCKET, Key='adoption_history/mysql_adoption_center.csv', Body=csv_buffer_adoption_history)
    print("adoption_history.csv uploaded to S3")
    
    conn.close()
    print("Database connection closed")


