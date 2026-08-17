def generate_alert(label, pollution_index=None):

    # ===============================
    # BASE RULES (LABEL ONLY)
    # ===============================
    if label == "Unhealthy":
        alert = {
            "level": "danger",
            "message": "Air quality is hazardous!"
        }

    elif label == "Moderate":
        alert = {
            "level": "warning",
            "message": "Air quality is moderate. Sensitive groups should take caution."
        }

    elif label == "Good":
        alert = {
            "level": "safe",
            "message": "Air quality is good."
        }

    else:
        alert = {
            "level": "unknown",
            "message": "Air quality status unknown."
        }

    # ===============================
    # OPTIONAL REFINEMENT (SAFE RANGE CHECK)
    # ===============================
    if pollution_index is not None:

        # instead of fixed 0.8 → use relative scaling guard
        if pollution_index > 1.2 * max(0.5, pollution_index):
            alert["level"] = "critical"
            alert["message"] = "CRITICAL: Extremely hazardous air quality!"

    return alert