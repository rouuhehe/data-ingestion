import os
import boto3
import psycopg2
import pandas as pd
from io import StringIO
from dotenv import load_dotenv

load_dotenv()
S3_BUCKET = os.getenv("S3_BUCKET")
ficheroUpload1 = "pets.csv"
ficheroUpload2 = "statuses.csv"
ficheroUpload3 = "vaccines.csv"
ficheroUpload4 = "centers.csv"

def export_postgres():
    s3 = boto3.client('s3')
    s3.upload_file(ficheroUpload1, S3_BUCKET, f'proyecto-parcial/postgres/{ficheroUpload1}')
    print("pets table was exported to S3")
    s3.upload_file(ficheroUpload2, S3_BUCKET, f'proyecto-parcial/postgres/{ficheroUpload2}')
    print("statuses table was exported to S3")
    s3.upload_file(ficheroUpload1, S3_BUCKET, f'proyecto-parcial/postgres/{ficheroUpload3}')
    print("vaccines table was exported to S3")
    s3.upload_file(ficheroUpload1, S3_BUCKET, f'proyecto-parcial/postgres/{ficheroUpload4}')
    print("centers table was exported to S3")

    print("Postgres export completed")

