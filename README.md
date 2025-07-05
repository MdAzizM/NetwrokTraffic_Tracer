# 🛰️ NetworkTraffic tracer

> A lightweight network traffic sniffer that logs unique IPs and resolves their DNS names in real-time.

---

## 📌 Overview

**NetworkTraffic Tracer** is a Python-based utility that captures live network packets, detects new IP addresses, performs reverse DNS lookups, and displays them in a live terminal table. It also logs all packet data and maintains a CSV file of known IPs.

This tool is perfect for network enthusiasts, cybersecurity learners, and anyone who wants to understand what's happening on their network.

---

## 🚀 Features

- 📡 Real-time packet sniffing using Scapy  
- 🌍 DNS resolution for IP addresses (if available)  
- 📊 Terminal table view of discovered hosts  
- 📝 Logging of all traffic to a file  
- 📂 CSV export of unique IPs and hostnames  
- ⏳ Animated scanning feedback in terminal  
- 🧱 Modular codebase for easy extension

---

## 📁 Project Structure
```bash
NetwrokTraffic_tracer/
├── main.py
├── run_sniffer.sh
├── Utils/
│ ├── sniffer.py
│ ├── ip_tracker.py
│ ├── display.py
│ └── protocols.py
├── known_ips.csv
├── logs.txt
├── requirements.txt
└── README.md
```
---

## ⚙️ Usage

⚠️ You must run the script with sudo/root privileges to capture packets:
```bash
bash run_sniffer.sh 
