from flask import Blueprint, request, jsonify

from services.sensor_service import process_sensor_data
from core.feature_engineering import create_features
from core.predictor import predict
from services.alert_service import generate_alert
from services.storage_service import store_data

sensor_bp = Blueprint("sensor", __name__)


@sensor_bp.route("/sensor", methods=["POST"])
def receive_sensor_data():

    data = request.json
    print("\n📥 Incoming Data:", data)

    device_id = data.get("device_id")
    mq = data.get("mq")

    print("📊 MQ Value:", mq)

    history, error = process_sensor_data(device_id, mq)

    features = create_features(mq, history)

    result = predict(features)

    print("🤖 Prediction:", result)

    label = result["label"]
    # pollution_index = result["pollution_index"]

    alert = generate_alert(label)

    return jsonify({
        "mq": mq,
        "label": label,
        
        "alert": alert
    })
    # "pollution_index": pollution_index,