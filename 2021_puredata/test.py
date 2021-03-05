#!/usr/bin/env python3

import socket
import os
import time
import random
import re

#PDPATH = "/Applications/Pd-l2ork.app/Contents/MacOS/nwjs main.pd &"
PDPATH = "pd main.pd &"
PATTERN1 = re.compile(r'file (.+);')
UDP_IP = "127.0.0.1"
UDP_SEND_PORT = 8000
UDP_RCV_PORT = 8001

if __name__ == "__main__":
    os.system(PDPATH)
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    """for _ in range(10):
        token = str.encode(str(random.randint(0, 100)))
        sock.sendto(token, (UDP_IP, UDP_PORT))
        print("send", token)
        time.sleep(1)"""

    # sock.close()

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
                sock_srv.sendto(b'received', ("127.0.0.1",8000))
        except KeyboardInterrupt:
            sock_srv.close()
            exit()
