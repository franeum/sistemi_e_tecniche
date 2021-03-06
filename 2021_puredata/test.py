#!/usr/bin/env python3

import socket
import os
import time
import random
import re
import sys

if sys.platform == 'darwin':
    PDPATH = "/Applications/Pd-l2ork.app/Contents/MacOS/nwjs main.pd &"
elif sys.platform == 'linux':
    PDPATH = "pd main.pd &"
elif sys.platform == 'win32':
    exit()

PATTERN1 = re.compile(r'file (.+);')
UDP_IP = "127.0.0.1"
UDP_SEND_PORT = 8000
UDP_RCV_PORT = 8001

if __name__ == "__main__":
    os.system(PDPATH)

    sock_srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    sock_srv.bind((UDP_IP, UDP_RCV_PORT))

    while True:
        try:
            data, addr = sock_srv.recvfrom(1024)
            data = data.decode("utf-8")
            print(data)
            print(addr)
            res = re.match(PATTERN1, data)
            if res:
                print(f"received message: {res.group(1)}")
                sock_srv.sendto(b'received', (UDP_IP, 8000))
        except KeyboardInterrupt:
            sock_srv.close()
            exit()
