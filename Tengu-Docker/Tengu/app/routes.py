
from flask import jsonify

def init_routes(app):
    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to the secure Flask Server!"})