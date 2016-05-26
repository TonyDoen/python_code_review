#!/usr/bin/python
#Filename: using_backup_v2.py

import os
import time

#1.
source = ['/home/tony1/test','/home/tony1/Downloads/teat2']
#2.
target_dir = '/home/tony1/bak/'
#3.
#4.
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print 'successfully created directory', today

target = today + os.sep + now + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'successfully backup to', target
else:
    print 'backup failed'
