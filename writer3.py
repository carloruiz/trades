import ctypes
import mmap
import os
import struct
import time
import signal
from config import *

def main():
    flag = 1
    def signal_handler(*args): nonlocal flag; flag = 0
    signal.signal(signal.SIGTERM, signal_handler)

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
        offset+=f.write(string.encode(encoding='ascii'))
        f.seek(offset % BUF)
        time.sleep(0.1)

        #if offset > MAP_SIZE - PADDING:
        #    f.seek(0)
        #    offset = 0

    buf.seek(0)
    buf.write((0).to_bytes(8, byteorder='big'))
    buf.close()
    f.close()
    os.close(fd) 
    os.close(fd2)
    print("successfully exited writer3")

if __name__ == '__main__':
    main()
 
