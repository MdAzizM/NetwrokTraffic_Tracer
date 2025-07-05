import csv
import socket

seen_ips = set()
ip_hostnames = {}
csv_file = "known_ips.csv"

def reverse_dns_lookup(ip):
    if ip in ip_hostnames:
        return ip_hostnames[ip]
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        hostname = None
    ip_hostnames[ip] = hostname
    return hostname


def is_new_ip(ip):
    if ip not in seen_ips:
        seen_ips.add(ip)
        reverse_dns_lookup(ip)
        return True
    return False

def get_all_ips():
    return sorted(seen_ips)

def get_hostname(ip):
    return ip_hostnames.get(ip, None)

def save_to_csv():
    with open(csv_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["No.", "IP Address", "Hostname"])
        for i, ip in enumerate(get_all_ips(), start=1):
            writer.writerow([i, ip, get_hostname(ip)])
