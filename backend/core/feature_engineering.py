import numpy as np
import pandas as pd
from datetime import datetime

WINDOW_SIZE = 10

FEATURE_ORDER = [
    "sensor_value", 
    "hour",
    "day",
    "month",
    "rolling_mean",
    "rolling_std",
    "lag_1",
    "lag_2",
    "source"
]


def create_features(mq, history, source=0):
    """
    STRICTLY MATCHES TRAINING FEATURES
    """

    now = datetime.now()

    # ===============================
    # SAFETY: ensure history exists
    # ===============================
    if history is None or len(history) == 0:
        history = [mq]

    # ===============================
    # Rolling window (fixed)
    # ===============================
    window = history[-WINDOW_SIZE:]

    rolling_mean = float(np.mean(window))
    rolling_std = float(np.std(window))

    # ===============================
    # Correct lag logic
    # ===============================
    # lag_1 = previous value
    # lag_2 = value before that

    lag_1 = history[-1] if len(history) >= 1 else mq
    lag_2 = history[-2] if len(history) >= 2 else lag_1

    features = {
        "sensor_value": mq,
        "hour": now.hour,
        "day": now.day,
        "month": now.month,
        "rolling_mean": rolling_mean,
        "rolling_std": rolling_std,
        "lag_1": lag_1,
        "lag_2": lag_2,
        "source": source
    }

    # ===============================
    # FORCE ORDER (VERY IMPORTANT)
    # ===============================
    return pd.DataFrame([[features[k] for k in FEATURE_ORDER]], columns=FEATURE_ORDER)