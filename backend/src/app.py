from application import create_app
from flask import jsonify
from waitress import serve
from utils import oidc

app = create_app('settings.py')
oidc.init_app(app)

@app.route('/api/health')
def health():
    return jsonify({"status": "ok"}), 200

serve(app, host="0.0.0.0", port=8000)