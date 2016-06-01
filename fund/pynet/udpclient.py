# -*- coding: utf-8 -*-

import socket

'''
1. open two terminal
2. python udpserver.py
3. python udpclient.py
'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect(('127.0.0.1', 9999))
#print s.recv(1024)
for data in ['michael', 'tracy', 'sarah'] :
    s.sendto(data, ('127.0.0.1', 9999))
    print s.recv(1024)
s.close()

