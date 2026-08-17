import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "air_quality_db"

# Storage control
STORE_INTERVAL_SECONDS = 60   # store every 1 minute

# History buffer
HISTORY_LIMIT = 30

# Alert thresholds (fallback if no AI)
MQ_DANGER_THRESHOLD = 2000

# Rate limiting
MIN_REQUEST_INTERVAL = 2  # seconds

ENV = "development"
DEBUG = True

