import os
import time

offset = 0
with open('IPC', 'wb') as f:
    while offset < 1024:
        f.write(offset.to_bytes(8, byteorder='big'))
        f.flush()
        f.seek(0)
        offset+=16
        time.sleep(1)
