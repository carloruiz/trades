import ctypes
import mmap
import os
import struct
import time
import signal

MAP_SIZE = 4096 #4194304
METAMAP_SIZE = 512

flag = 1
def signal_handler(signal, frame):
    flag = 0

signal.signal(signal.SIGINT, signal_handler)

# the big, output map
fd = os.open('sharedMap', os.O_RDWR)
f = mmap.mmap(fd, MAP_SIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)

# the small IPC map with metadata
fd2 = os.open('metaMap', os.O_RDWR)
buf = mmap.mmap(fd2, METAMAP_SIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)


offset = 0
while flag:
    buf.seek(0)
    buf.write(offset.to_bytes(8, byteorder='big'))
    string = "offset currently at %d\n" % offset
    n = f.write(string.encode(encoding='ascii'))
    offset += n
    if offset > 3800:
        f.seek(0)
        offset = 0
    time.sleep(0.1)

buf.close()
f.close()
os.close(fd) 
os.close(fd2)
