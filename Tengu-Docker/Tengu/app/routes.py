
from flask import jsonify, render_template, send_from_directory, abort
import os

"""
    # Serve any file from the 'templates' directory
    @app.route('/<path:subpath>/<filename>')
    def serve_file(subpath, filename):
        # Define the path to the template folder
        directory = os.path.join(app.root_path, 'templates', subpath)

        # Check if the directory exists and the file exists
        if os.path.isdir(directory) and os.path.exists(os.path.join(directory, filename)):
            # Serve the file from the directory
            return send_from_directory(directory, filename)
        else:
            # If the directory or file does not exist, return a 404
            abort(404)
"""

def init_routes(app):
    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to the secure Flask Server!"})
    
    # Serve any file from the 'templates' directory
    @app.route('/<path:subpath>/<filename>')
    @app.route('/<filename>', defaults={'subpath': ''})
    def serve_file(subpath, filename):
        # Define the path to the template folder
        directory = os.path.join(app.root_path, 'templates', subpath)

        # Handle the case where the file is in the root templates folder (no subpath)
        if not subpath:
            directory = os.path.join(app.root_path, 'templates')

        # Check if the directory exists and the file exists
        if os.path.exists(os.path.join(directory, filename)):
            # Serve the file from the directory
            return send_from_directory(directory, filename)
        else:
            # If the directory or file does not exist, return a 404
            abort(404)