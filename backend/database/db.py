from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

try:
    client.server_info()  # forces connection check
except Exception as e:
    print(f"[DB ERROR] MongoDB connection failed: {e}")

db = client[DB_NAME]

sensor_collection = db["sensor_data"]