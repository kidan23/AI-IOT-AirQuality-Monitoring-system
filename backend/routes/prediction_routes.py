from flask import Blueprint, request, jsonify

from services.sensor_service import process_sensor_data
from core.feature_engineering import create_features
from core.predictor import predict
from services.alert_service import generate_alert

prediction_bp = Blueprint("prediction", __name__)


@prediction_bp.route("/predict", methods=["POST"])
def manual_predict():

    data = request.json
    mq = data.get("mq")

    if mq is None:
        return jsonify({"error": "mq required"}), 400

    device_id = data.get("device_id", "manual")

    history, error = process_sensor_data(device_id, mq)

    if error:
        return jsonify({"error": error}), 429

    # STEP 1: features
    features = create_features(mq, history)

    # STEP 2: prediction
    result = predict(features)

    label = result["label"]
    pollution_index = result["pollution_index"]

    # STEP 3: alert
    alert = generate_alert(label)

    return jsonify({
        "mq": mq,
        "label": label,
        "pollution_index": pollution_index,
        "alert": alert
    })