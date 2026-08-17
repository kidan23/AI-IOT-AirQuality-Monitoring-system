import time
from config import HISTORY_LIMIT, MIN_REQUEST_INTERVAL

device_history = {}
last_request_time = {}


def process_sensor_data(device_id, mq):

    now = time.time()

    # rate limiting
    if device_id in last_request_time:
        if now - last_request_time[device_id] < MIN_REQUEST_INTERVAL:
            return None, "Too many requests"

    last_request_time[device_id] = now

    # init history
    if device_id not in device_history:
        device_history[device_id] = []

    history = device_history[device_id]

    history.append(mq)

    # maintain window
    if len(history) > HISTORY_LIMIT:
        history.pop(0)

    return history, None