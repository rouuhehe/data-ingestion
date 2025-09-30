import os
import boto3
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
S3_BUCKET = os.getenv("S3_BUCKET")
ficheroUpload = "histories.json"

def export_mongo():
    s3 = boto3.client('s3')
    s3.upload_file(ficheroUpload, S3_BUCKET, f'proyecto-parcial/mongo/{ficheroUpload}')
    print("Mongo collection was exported to S3")

