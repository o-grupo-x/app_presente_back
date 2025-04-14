from application import create_app
from flask import jsonify  # Add this import
from waitress import serve
from utils import oidc

app = create_app('settings.py')
oidc.init_app(app)

@app.route('/health')  # Use /health for HEALTHCHECK
def health():
    return jsonify({"status": "ok"}), 200

serve(app, host="0.0.0.0", port=8000)