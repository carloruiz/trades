import mmap
import os
import struct
import time
import signal
import sys

MAP_SIZE = 4096 #4194304
METAMAP_SIZE = 512

time.sleep(0.5)
flag = 1

def signal_handler(signal, frame):
    flag = 0

signal.signal(signal.SIGINT, signal_handler)

# small IPC map
fd = os.open('metaMap', os.O_RDONLY)
buf = mmap.mmap(fd, METAMAP_SIZE, mmap.MAP_SHARED, mmap.PROT_READ)

# larger output file
fd2 = os.open('sharedMap', os.O_RDONLY)
f = mmap.mmap(fd2, MAP_SIZE, mmap.MAP_SHARED, mmap.PROT_READ)

new = prev = 0
while flag:
    while new == prev and flag:
        new = int.from_bytes(buf[:8], byteorder='big')
    
    if not flag:
        break


    line = f.readline()
    print(line)
    try:
        assert(prev + len(line) == new)
    except AssertionError:
        print('prev + len(line) = %d != %d = new' % ((prev + len(line)), new))
       # sys.exit(1)
    
    prev = new
    if new > 3800:
        f.seek(0)
        prev = new = 0


buf.close()
f.close()
os.close(fd2)
os.close(fd)
    


