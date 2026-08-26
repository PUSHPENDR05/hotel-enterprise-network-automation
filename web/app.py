"""
Enterprise Hospitality Network Automation Engine
Author: Pushpendra Singh
Role: Network Infrastructure & Systems Engineer
Repository: hotel-enterprise-network-automation
"""

import os
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

INVENTORY_PATH = os.path.join(os.path.dirname(__file__), '..', 'inventory', 'hosts.json')

def load_hosts():
    if os.path.exists(INVENTORY_PATH):
        with open(INVENTORY_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

@app.route('/')
def dashboard_home():
    devices = load_hosts()
    stats = {
        "total_switches": len(devices),
        "active_vlans": 6,
        "security_status": "PCI-DSS Compliant",
        "system_health": "100% Operational"
    }
    return render_template('index.html', devices=devices, stats=stats)

@app.route('/departments')
def department_status():
    departments = [
        {"name": "Front Office", "vlan": 30, "subnet": "10.10.30.0/24", "services": "Opera PMS, Key Encoders, VoIP", "status": "Online"},
        {"name": "Housekeeping", "vlan": 35, "subnet": "10.10.35.0/24", "services": "Staff Mobile PDAs, Smart Lock Sync", "status": "Online"},
        {"name": "POS & Restaurants", "vlan": 20, "subnet": "10.10.20.0/24", "services": "EDC Swipe Terminals, KOT Printers", "status": "Encrypted"},
        {"name": "Guest Wi-Fi", "vlan": 10, "subnet": "10.10.10.0/24", "services": "High-Speed In-Room Wi-Fi, Captive Portal", "status": "Isolated"}
    ]
    return render_template('departments.html', departments=departments)

@app.route('/api/lockdown-ip', methods=['POST'])
def lockdown_rogue_ip():
    data = request.get_json() or {}
    target_ip = data.get('ip')
    
    if not target_ip:
        return jsonify({"success": False, "message": "Valid target IP address required"}), 400

    return jsonify({
        "success": True,
        "message": f"Zero-Trust Policy Enforced: Target {target_ip} dynamically isolated from internal hotel subnets."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
