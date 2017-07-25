import sys
import time

with open('out.txt') as f:
    while True:
        line = f.readline()
        if line:
            print("[reader1.py]: %s" % line)    
        else:
            time.sleep(0.5)
