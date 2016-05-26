#!/usr/bin/python
#Filename: using_try_finally1.py

import time

try:
    f = file('poem.txt') 
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2) #stop 2 sec
        print line,
finally:
    f.close()
    print 'clean up, closed the file.'
