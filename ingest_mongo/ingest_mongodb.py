import os
import boto3
from bson import json_util
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

S3_BUCKET = os.getenv("S3_BUCKET")

def export_mongo():
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]

    docs = list(collection.find())
    print(f"Fetched {len(docs)} documents from MongoDB")

    docs_json = json_util.dumps(docs)

    s3 = boto3.client('s3')
    s3.put_object(Bucket=S3_BUCKET, Key='pets/mongo_pets.json', Body=docs_json)
    print("pets.json uploaded to S3")

    client.close()
    print("Mongo collection was exported to S3")

