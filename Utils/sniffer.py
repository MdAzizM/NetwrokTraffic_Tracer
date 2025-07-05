from scapy.all import sniff, IP
from datetime import datetime
from .ip_tracker import is_new_ip, save_to_csv
from .display import print_ip_table
from .protocole import protocol_table

def handle_packet(packet):
    if IP in packet:

        ADDr = packet[IP]

        proto_num = ADDr.proto
        src = ADDr.src
        dst = ADDr.dst
        now = datetime.now().strftime('%H:%M:%S')


        proto_name = protocol_table.get(proto_num, f"OTHER({proto_num})")

        
        log_line = f"[{now}]: {proto_name} {src} -> {dst}"

        with open("logs.txt", "a") as f:
            f.write(log_line + "\n")

        if is_new_ip(src) or is_new_ip(dst):
            print_ip_table()
            save_to_csv()

def start_sniffing():
    sniff(filter="ip", prn=handle_packet, store=0)
