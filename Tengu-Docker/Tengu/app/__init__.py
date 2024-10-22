
from flask import Flask
from .middlewares import block_requests
from .logger import log_request

def create_app():
    # Initialise Flask app
    app = Flask(__name__)

    # Register middleware for blocking
    app.before_request(block_requests)

    # Register middleware for logging requests
    app.after_request(log_request)

    # Import routes
    from .routes import init_routes
    init_routes(app)

    return app