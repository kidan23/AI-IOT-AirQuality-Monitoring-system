import joblib
import os

# ===============================
# PATHS
# ===============================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "smart_airquality_model(9).pkl")
QUANTILES_PATH = os.path.join(BASE_DIR, "models", "quantiles.pkl")


# ===============================
# LOAD ARTIFACTS (ONCE ONLY)
# ===============================
model = joblib.load(MODEL_PATH)
q1, q2 = joblib.load(QUANTILES_PATH)


# ===============================
# ACCESS FUNCTIONS (SAFE IMPORTS)
# ===============================
def get_model():
    return model


def get_quantiles():
    return q1, q2