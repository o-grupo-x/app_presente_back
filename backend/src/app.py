from application import create_app
from flask import jsonify
from waitress import serve
from utils import oidc

app = create_app('settings.py')
oidc.init_app(app)

@app.route('/api/health')
def health():
    return jsonify({"status": "okk Laercio is on fire e fabio is on fire também"}), 200

print("🚀 Versão de teste de deploy: v1.0.4")

serve(app, host="0.0.0.0", port=8000)
