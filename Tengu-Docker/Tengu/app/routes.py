
from flask import jsonify, render_template

def init_routes(app):
    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to the secure Flask Server!"})
    
    @app.route("/test")
    def test():
        return render_template('test.html')