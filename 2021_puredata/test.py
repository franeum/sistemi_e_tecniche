#!/usr/bin/env python3

import socket
import os
import time
import random
import re

PDPATH = "/Applications/Pd-l2ork.app/Contents/MacOS/nwjs main.pd &"
PATTERN1 = re.compile(r'file (.+);')
UDP_IP = "127.0.0.1"
UDP_PORT = 8001

if __name__ == "__main__":
    os.system(PDPATH)
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    """for _ in range(10):
        token = str.encode(str(random.randint(0, 100)))
        sock.sendto(token, (UDP_IP, UDP_PORT))
        print("send", token)
        time.sleep(1)"""

    # sock.close()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        try:
            data, addr = sock.recvfrom(1024)
            data = data.decode("utf-8")
            print(data)
            res = re.match(PATTERN1, data)
            if res:
                print(f"received message: {res.group(1)}")
        except KeyboardInterrupt:
            sock.close()
            exit()
