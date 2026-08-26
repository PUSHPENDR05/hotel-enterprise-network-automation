# Enterprise Hospitality Network Infrastructure & NetOps Automation Engine

[![Network Standard](https://img.shields.io/badge/Security-PCI--DSS%204.0%20Compliant-green.svg)]()
[![Topology](https://img.shields.io/badge/Infrastructure-Layer--3%20Core%20%2F%20IDF%20Distribution-blue.svg)]()
[![Stack](https://img.shields.io/badge/Stack-Cisco%20IOS%20%7C%20Python%20%7C%20Flask-orange.svg)]()

A production-grade network architecture designed and automated for a high-availability enterprise hospitality environment.

## VLAN & Subnet Architecture
| Segment Name | VLAN ID | Subnet CIDR | Default Gateway | Security Zone |
|---|---|---|---|---|
| Guest Wi-Fi | VLAN 10 | 10.10.10.0/24 | 10.10.10.1 | Isolated |
| POS & Billing | VLAN 20 | 10.10.20.0/24 | 10.10.20.1 | PCI-DSS Secure |
| Front Office | VLAN 30 | 10.10.30.0/24 | 10.10.30.1 | Operational Core |
| Housekeeping | VLAN 35 | 10.10.35.0/24 | 10.10.35.1 | Internal Ops |

## Repository Structure
- inventory/hosts.json
- topology/hotel_network.pkt
- web/app.py
- web/templates/
