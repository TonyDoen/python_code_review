# -*- coding: utf-8 -*-

import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn', 80))
# 发送数据
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True :
    d = s.recv(1024)
    if d :
        buffer.append(d)
    else :
        break
data = ''.join(buffer)
s.close()

header, html = data.split('\r\n\r\n', 1)
print header

with open('sina.html', 'wb') as f :
    f.write(html)
