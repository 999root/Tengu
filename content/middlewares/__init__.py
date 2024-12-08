
# /content/middlewares/__init__.py
from flask import *

# Pull Api
from ..api.asn import *


# User Agents
def block_ua_middleware():
    ua = request.user_agent.string
    banned_user_agents = pull_user_agent_contents()
    if ua in banned_user_agents:
        return jsonify({"Error", "Blocked User Agent"}), 403
    