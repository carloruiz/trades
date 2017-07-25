import os
import time

num = 0
with open('out.txt', 'w') as f:
    while(num < 25):
        f.write("counter at %d\n" % num)
        f.flush()
        num+=1
        time.sleep(1)


