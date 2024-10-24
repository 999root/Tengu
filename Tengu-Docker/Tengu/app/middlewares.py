import requests
from flask import request, abort

from .lists import load

# Blocked lists
blocked_ips = load.IP.load()
blocked_asns = load.ASN.load()
blocked_user_agents = load.UA.load()
blocked_referers = load.REF.load()

# Function to block IPs
def is_ip_blocked(ip):
    return ip in blocked_ips

# Function to get ASN via API (IPinfo)
def get_asn_from_ip(ip):
    try:
        # Call the IPinfo API to get ASN information
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()

        # Extract ASN from response (e.g., "AS12345")
        asn_str = data.get('org', '')
        if asn_str.startswith("AS"):
            return int(asn_str[2:])  # Convert "AS12345" -> 12345
        return None
    except Exception as e:
        print(f"Failed to retrieve ASN for IP {ip}: {e}")
        return None

# Function to block ASNs
def is_asn_blocked(ip):
    asn = get_asn_from_ip(ip)
    if asn:
        return asn in blocked_asns
    return False

# Function to block User Agents
def is_user_agent_blocked(user_agent):
    for blocked_agent in blocked_user_agents:
        if blocked_agent.lower() in user_agent.lower():
            return True
    return False

# Function to block Referers
def is_referer_blocked(referer):
    for blocked_referer in blocked_referers:
        if blocked_referer.lower() in referer.lower():
            return True
    return False

# Middleware to block requests
def block_requests():
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent", "")
    referer = request.headers.get("Referer", "")
    
    if is_ip_blocked(ip):
        abort(403, description="Access denied: IP blocked")
    
    if is_asn_blocked(ip):
        abort(403, description="Access denied: ASN blocked")
    
    if is_user_agent_blocked(user_agent):
        abort(403, description="Access denied: User Agent blocked")
    
    if is_referer_blocked(referer):
        abort(403, description="Access denied: Referer blocked")
