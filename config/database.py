from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client["library_db"]

collection_name = db["student_info"]
