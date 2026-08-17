import time
from database.db import sensor_collection


def store_data(device_id, mq, features, label, pollution_index=None):

    try:
        sensor_collection.insert_one({
            "device_id": device_id,
            "mq": mq,
            "features": features,
            "label": label,
            "pollution_index": pollution_index,
            "timestamp": time.time()
        })

    except Exception as e:
        print(f"[DB ERROR] Failed to store data: {e}")