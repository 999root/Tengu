
# content/api/__init__.py
from flask import Blueprint

# CXreate blueprint for the API
api_blueprint = Blueprint('api', __name__)

# Import Routes
from .asn import *