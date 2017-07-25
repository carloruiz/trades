import ctypes
import mmap
import os
import struct
import time

fd = os.open('map', os.O_CREAT | os.O_TRUNC | os.O_RDWR)
assert(os.write(fd, bytearray(mmap.PAGESIZE)) == mmap.PAGESIZE)
buf = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)

offset = 0
while offset < 1024:
    buf.seek(0)
    buf.write(offset.to_bytes(8, byteorder='big'))
    offset+=16
    time.sleep(0.1)

buf.close()
os.close(fd) 
