def classify(mq):
    if mq <= 500:
        return "Good"
    elif mq <= 750:
        return "Moderate"
    else:
        return "Unhealthy"