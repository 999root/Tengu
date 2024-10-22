
import os
import json
from flask import request
from datetime import datetime, timezone
from .middlewares import get_asn_from_ip

# Log file location
log_folder = 'logs'
log_file = os.path.join(log_folder, 'requests.log.json')

# Ensure the log directory exists
def log_request(response):
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "ip": request.remote_addr,
        "asn": get_asn_from_ip(request.remote_addr),
        "method": request.method,
        "path": request.path,
        "status_code": response.status_code,
        "user_agent": request.headers.get("User-Agent")
    }

    # Write the log entry to the .json log file

    with open(log_file, 'a') as f:
        json.dump(log_entry, f)
        f.write('\n')

    return response