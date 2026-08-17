def format_response(label, alert, mq, pollution_index=None):

    response = {
        "mq": mq,
        "label": label,
        "status": alert["level"],
        "message": alert["message"]
    }

    if pollution_index is not None:
        response["pollution_index"] = round(pollution_index, 3)

    return response