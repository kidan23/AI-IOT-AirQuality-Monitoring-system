# from flask import Blueprint, render_template
# from database.db import sensor_collection
# from utils.helper import format_timestamp

# dashboard_bp = Blueprint("dashboard", __name__)


# @dashboard_bp.route("/")
# def dashboard():

#     raw_data = list(sensor_collection.find().sort("timestamp", -1).limit(50))

#     data = []

#     for d in raw_data:
#         data.append({
#             "device_id": d.get("device_id"),
#             "mq": d.get("mq"),
#             "label": d.get("label"),
#             "pollution_index": d.get("pollution_index"),
#             "timestamp": format_timestamp(d.get("timestamp", 0))
#         })

#     return render_template("dashboard.html", data=data)

from flask import Blueprint, render_template, jsonify
from database.db import sensor_collection
from utils.helper import format_timestamp
import time

# dashboard_bp = Blueprint("dashboard", __name__)
import os
dashboard_bp = Blueprint(
    "dashboard", __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'dashboard', 'templates')
)


def _build_record(d):
    """Convert a MongoDB document to a clean dict for the dashboard."""
    ts = d.get("timestamp", 0)
    # timestamp may already be a formatted string (from aggregator.py)
    if isinstance(ts, str):
        formatted_ts = ts
    else:
        try:
            formatted_ts = format_timestamp(float(ts))
        except Exception:
            formatted_ts = str(ts)

    prediction = d.get("prediction") or {}
    label = d.get("label") or (prediction.get("label") if isinstance(prediction, dict) else None) or "unknown"
    pollution_index = d.get("pollution_index") or (prediction.get("pollution_index") if isinstance(prediction, dict) else None)

    return {
        "device_id": d.get("device_id", "—"),
        "mq": d.get("mq", 0),
        "label": label,
        "pollution_index": pollution_index,
        "timestamp": formatted_ts,
    }


@dashboard_bp.route("/")
def dashboard():
    raw_data = list(sensor_collection.find().sort("timestamp", -1).limit(50))
    data = [_build_record(d) for d in raw_data]
    return render_template("dashboard.html", data=data)


@dashboard_bp.route("/api/latest")
def api_latest():
    """JSON endpoint polled by the dashboard frontend every 5 seconds."""
    raw_data = list(sensor_collection.find().sort("timestamp", -1).limit(50))
    data = [_build_record(d) for d in raw_data]
    return jsonify(data)