
# content/views/__init__.py
from flask import Blueprint

# CXreate blueprint for the API
views_blueprint = Blueprint('views', __name__, template_folder="../../templates")

# Import Routes
from . import dashboard