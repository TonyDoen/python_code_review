#!/usr/bin/python
#Filename: using_backup_v1.py

import os
import time

#1.
source = ['/home/tony1/test', '/home/tony1/Downloads/teat2']
#2.
target_dir = '/home/tony1/bak/'
#3.
#4.
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
#5.
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

#run
if os.system(zip_command) == 0:
    print 'successful backup to', target
else:
    print 'backup failed'
