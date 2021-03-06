#!/usr/bin/env python3

import socket
import os
import time
import random
import re
import sys
import librosa 

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

filename_pattern = re.compile(r"filename (.+);")
samplerate_pattern = re.compile(r"samplerate (.+);")
filename = None 
samplerate = None 

def get_filename(data):
    res = re.match(filename_pattern, data)

    if res is not None:
        return res.group(1) 


def get_samplerate(data):
    res = re.match(samplerate_pattern, data) 

    if res is not None:
        return int(res.group(1))


def process_audio():
    y, sr = librosa.load(filename, sr=samplerate)
    o_env = librosa.onset.onset_strength(y, sr=sr)
    times = librosa.times_like(o_env, sr=sr)
    tempo = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr, hop_length=16)
    beat_times = librosa.frames_to_time(tempo, sr=sr)
    offset_words = int(len(y) / len(tempo) / sr)
    nr_of_words = len(beat_times)
    return offset_words, nr_of_words


if __name__ == "__main__":
    os.system(PDPATH)
    sock_srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    sock_srv.bind((UDP_IP, UDP_RCV_PORT))

    while True:
        try:
            data, addr = sock_srv.recvfrom(1024)
            data = data.decode("utf-8")
            
            # sock_srv.sendto(b'received', (UDP_IP, 8000))"""

            f_name = get_filename(data)
            f_sr = get_samplerate(data)
            
            if f_name:
                filename = f_name 

            if f_sr:
                samplerate = f_sr 

            if filename and samplerate:
                offset, nr_words = process_audio()

                offset = f"offset_words {offset}"
                nr_words = f"nr_words {nr_words}"

                sock_srv.sendto(str.encode(offset), (UDP_IP, UDP_SEND_PORT))
                sock_srv.sendto(str.encode(nr_words), (UDP_IP, UDP_SEND_PORT))

        except KeyboardInterrupt:
            sock_srv.close()
            print("filename", filename)
            print("samplerate", samplerate)
            exit()
