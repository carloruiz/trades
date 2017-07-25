import mmap
import os
import struct
import time

time.sleep(0.5)
fd = os.open('map', os.O_RDONLY)
buf = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_READ)

new = prev  = 0
while new < 1008:
    while new == prev:
        new  = int.from_bytes(buf[:8], byteorder='big')
        
    print('I have offset = %d' % new)
    prev = new

buf.close()
os.close(fd)
    


