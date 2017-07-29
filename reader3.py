import mmap
import os
import struct
import time
import signal
import sys
from config import *

#time.sleep(0.5)

def main():
    flag = 1
    def signal_handler(*args): nonlocal flag; flag = 0
    signal.signal(signal.SIGTERM, signal_handler)

    # small IPC map
    fd = os.open('metaMap', os.O_RDONLY)
    buf = mmap.mmap(fd, METAMAP_SIZE, mmap.MAP_SHARED, mmap.PROT_READ)

    # larger output file
    fd2 = os.open('sharedMap', os.O_RDONLY)
    f = mmap.mmap(fd2, MAP_SIZE, mmap.MAP_SHARED, mmap.PROT_READ)

    offset = my_pos = int.from_bytes(buf[:8], byteorder='big')
    print("offset at: %d" % offset)
    f.seek(my_pos % BUF)

    while flag:
        while offset == my_pos and flag:
            offset = int.from_bytes(buf[:8], byteorder='big')
        
        if not flag:
            break

        line = f.readline()
        print(line)
       
        my_pos+=len(line) 
        f.seek(my_pos % BUF)
    
    buf.close()
    f.close()
    os.close(fd2)
    os.close(fd)
    print("successfully exited reader3")
    
if __name__ == '__main__':
    main()

