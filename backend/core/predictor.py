import pandas as pd
from core.model import get_model
from core.label_mapper import classify

model = get_model()


def predict(features):

    # Ensure DataFrame
    if isinstance(features, dict):
        features = pd.DataFrame([features])
    elif not isinstance(features, pd.DataFrame):
        features = pd.DataFrame(features)

    # Prediction
    pollution_index = float(model.predict(features)[0])

    # IMPORTANT: use raw MQ only
    mq_value = float(features['sensor_value'].iloc[0])

    # Classification (RULE-BASED)
    label = classify(mq_value)

    return {
        # "pollution_index": pollution_index,
        "label": label
    }