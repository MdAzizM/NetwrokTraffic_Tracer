#!/usr/bin/env python3

from Utils.sniffer import start_sniffing
import threading
import itertools
import time
import os
import sys

def scanning_animation():
    spinner = itertools.cycle(['[*] Scanning.  ', '[*] Scanning.. ', '[*] Scanning...'])
    while True:
        print(next(spinner), end='\r')
        time.sleep(0.5)

if __name__ == "__main__":
    os.system("clear")

    # Start blinking scanning banner in background
    animation_thread = threading.Thread(target=scanning_animation, daemon=True)
    animation_thread.start()

    try:
        start_sniffing()
    except KeyboardInterrupt:
        print("\n[!] Sniffing stopped.")
        sys.exit(0)
