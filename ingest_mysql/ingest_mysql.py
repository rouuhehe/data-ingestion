import os
import boto3
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
S3_BUCKET = os.getenv("S3_BUCKET")
ficheroUpload1 = "requests.csv"
ficheroUpload2 = "users.csv"

def export_mysql():
    s3 = boto3.client('s3')
    s3.upload_file(ficheroUpload1, S3_BUCKET, f'proyecto-parcial/mysql/{ficheroUpload1}')
    print("requests table was exported to S3")
    s3.upload_file(ficheroUpload2, S3_BUCKET, f'proyecto-parcial/mysql/{ficheroUpload2}')
    print("users table was exported to S3")
    print("Mysql collection was exported to S3")



