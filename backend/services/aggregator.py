import time
from database.db import sensor_collection
from config import STORE_INTERVAL_SECONDS

last_store_time = {}


def should_store(device_id):
    now = time.time()

    if device_id not in last_store_time:
        last_store_time[device_id] = now
        return True

    if now - last_store_time[device_id] >= STORE_INTERVAL_SECONDS:
        last_store_time[device_id] = now
        return True

    return False


def store_data(device_id, mq, features, prediction):

    sensor_collection.insert_one({
        "device_id": device_id,
        "mq": float(mq),
        "features": features,
        "prediction": prediction,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    })