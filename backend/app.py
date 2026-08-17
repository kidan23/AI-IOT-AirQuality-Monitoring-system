from flask import Flask, jsonify
from flask_cors import CORS

from routes.sensor_routes import sensor_bp
from routes.prediction_routes import prediction_bp
from routes.dashboard_routes import dashboard_bp
from services.scheduler import start_scheduler


def create_app():
    app = Flask(__name__)

    # =========================
    # Enable CORS
    # =========================
    CORS(app)

    # =========================
    # Register Blueprints
    # =========================
    app.register_blueprint(sensor_bp, url_prefix="/api")
    app.register_blueprint(prediction_bp, url_prefix="/api")
    app.register_blueprint(dashboard_bp)

    # =========================
    # Health Check
    # =========================
    @app.route("/health")
    def health():
        return jsonify({"status": "running"})

    # =========================
    # Error Handler
    # =========================
    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({
            "error": "internal server error"
        }), 500

    return app


# =========================
# App Initialization
# =========================
app = create_app()


def initialize_system():
    """
    All background services should start here
    (scheduler, monitoring, etc.)
    """
    print("🚀 System initializing...")

    start_scheduler()

    print("✅ System initialized successfully")


initialize_system()


# =========================
# Run Server
# =========================
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )