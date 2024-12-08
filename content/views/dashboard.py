
# content/views/routes/dashboard.py
from . import views_blueprint
from flask import *

# Import Middlewares
from ..middlewares import *

# Security Checks
@views_blueprint.before_request
def block_ua():
    return block_ua_middleware()

# Page
@views_blueprint.route("/", methods=["GET", "POST"]) 
def dashboard():
    return render_template("dashboard.html")