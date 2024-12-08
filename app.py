
# Import Flask 
from flask import * 

# Import Blueprint
from content import *

# Initialise the App
app = Flask(__name__)

# Register Blueprints
app.register_blueprint(api_blueprint, url_prefix="/api")
app.register_blueprint(views_blueprint)

# Deploy Flask on execution of app.py
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")