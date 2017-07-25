import sys
import time

with open('IPC', 'rb') as f:
    while True:
        f.seek(0)
        offset = int.from_bytes(f.read(8), byteorder='big')
        print("offset currently at: %d" % offset)   
        time.sleep(0.5)
