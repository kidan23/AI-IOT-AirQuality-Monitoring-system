import pandas as pd
from database.db import sensor_collection

def export_to_csv():
    data = list(sensor_collection.find())
    df = pd.DataFrame(data)
    df.to_csv("training_data.csv", index=False)