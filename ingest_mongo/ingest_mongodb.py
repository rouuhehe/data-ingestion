import os
import boto3
from dotenv import load_dotenv
from pymongo import MongoClient
import json
from io import BytesIO

load_dotenv()

# Config S3
S3_BUCKET = os.getenv("S3_BUCKET")
s3 = boto3.client("s3")

# Config Mongo
MONGO_URI = os.getenv("MONGO_URI") 
client = MongoClient(MONGO_URI)
db = client.get_database() 
collection_name = "histories"
collection = db[collection_name]

data = list(collection.find({}))

json_bytes = BytesIO(json.dumps(data, default=str).encode("utf-8"))

s3.upload_fileobj(json_bytes, S3_BUCKET, f"mongodb/{collection_name}.json")
print("Mongo collection was exported to S3")
