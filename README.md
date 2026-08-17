# AI-Based Air Quality Monitoring System

An IoT + Machine Learning system that monitors air quality in real time. An ESP32 microcontroller streams gas sensor (MQ) readings to a Flask backend, which runs them through a trained ML model to classify air quality (Good / Moderate / Unhealthy), triggers alerts, stores history in MongoDB, and serves the results to a live React dashboard.

## Features

- 📡 **Real-time ingestion** of sensor data from an ESP32 device over HTTP
- 🤖 **ML-based classification** of air quality using a trained scikit-learn model
- 🚨 **Automated alerts** with severity levels (safe / warning / danger / critical)
- 📊 **Live dashboard** (React + Vite) with charts, gauges, and per-device status
- 🗄️ **MongoDB storage** of historical sensor readings and predictions
- ⏱️ **Scheduled aggregation** via APScheduler for periodic data rollups

## Architecture

```
ESP32 Sensor  --->  Flask Backend  --->  MongoDB
  (MQ sensor)        - REST API           (readings + predictions)
                      - ML prediction
                      - Alert generation
                            |
                            v
                     React Dashboard
                    (live charts, gauges, alerts)
```

## Tech Stack

**Backend**
- Python, Flask, Flask-CORS
- scikit-learn, pandas, numpy (ML inference)
- PyMongo (MongoDB)
- APScheduler (scheduled tasks)
- Gunicorn (production server)

**Frontend**
- React 19 + Vite (landing page / frontend)
- React + Recharts (dashboard with live charts and gauges)

**Hardware**
- ESP32 microcontroller
- MQ-series gas sensor

## Project Structure

```
AI_IOT_air_quality_monitoring_system/
├── backend/
│   ├── app.py                # Flask app entry point
│   ├── config.py             # App configuration
│   ├── requirements.txt      # Python dependencies
│   ├── core/                 # Feature engineering, prediction, labeling
│   ├── models/                # Trained ML model (not included — see below)
│   ├── routes/                # API endpoints (sensor, prediction, dashboard)
│   ├── services/              # Business logic (aggregation, alerts, storage, scheduler)
│   ├── alerts/                 # ESP32 response formatting
│   ├── database/              # MongoDB connection & schemas
│   └── dashboard/              # Server-rendered dashboard template (legacy)
├── frontend/                   # React + Vite landing/frontend app
└── dashboard/                  # React dashboard (live monitoring UI)
```

## Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+
- MongoDB (local or Atlas)

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

Create a `.env` file in `backend/`:

```
MONGO_URI=mongodb://localhost:27017
```

Run the server:

```bash
python app.py
```

The API will be available at `http://localhost:5000`.

### Dashboard Setup

```bash
cd dashboard
npm install
npm run dev
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## ML Model

The trained model file (`smart_airquality_model.pkl`, ~112MB) is **not included in this repository** due to GitHub's file size limits.

To run predictions locally:
1. Download the model from **[add your hosting link — e.g. Google Drive / Hugging Face]**
2. Place it in `backend/models/`
3. Update the filename reference in `backend/core/predictor.py` if needed

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/api/sensor` | Receive sensor reading from ESP32, returns prediction + alert |
| POST | `/api/predict` | Manually submit an MQ value for prediction |
| GET | `/api/latest` | Poll latest readings for the dashboard |

## Background

This project was developed as part of the **SafeBreath** initiative during the SEED Cohort 7 Startup Incubation Program at Orbit Innovation Hub (in partnership with the Mastercard Foundation).

## Author

**Kidan** — [github.com/kidan23](https://github.com/kidan23)