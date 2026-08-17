import time
from database.db import sensor_collection

def store_data(device_id, mq, features, prediction):
    sensor_collection.insert_one({
        "device_id": device_id,
        "mq": mq,
        "features": features,
        "prediction": prediction,
        "timestamp": time.time()
    })