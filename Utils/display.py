from tabulate import tabulate
from .ip_tracker import get_all_ips, get_hostname
import os

def print_ip_table():
    os.system("clear")
    ips = get_all_ips()
    table = []
    for i, ip in enumerate(ips, start=1):
        hostname = get_hostname(ip) or "-"
        table.append((i, ip, hostname))
    print("=== Known IPs ===")
    print(tabulate(table, headers=["No.", "IP Address", "Hostname"]))

