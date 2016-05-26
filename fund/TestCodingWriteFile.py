# -*- coding:utf8 -*-

def wfile(fname,fcontent):
    try:
        f = open(fname, 'w+')
    except IOError, e:
        print 'error:', e
    else:
        f.write(fcontent)
    finally:
        f.close()

from os import path
def rfile(fname):
    if path.exists(fname):
        try:
            f = open(fname, 'r+')
        except IOError, e:
            print 'error:', e
        else:
            for line in f:
                print line
        finally:
            f.close()




content = u'\u662f\u591c\u6e05\u5bd2\uff0c\u4f59\u5453\uff0c\u516b\u5e74\u524d\u5140\u81ea\u4e00\u4eba\uff0c\u5c1d\u602a\u8bde\u3002\u516d\u5e74\u524d\uff0c\u7a77\u5b51\u72ec\u7acb\uff0c\u611a\u4e14\u50b2\u3002\u56db\u5e74\u524d\uff0c\u90c1\u90c1\u5b64\u884c\uff0c\u5e38\u6e05\u8c08\u3002\u4e24\u5e74\u524d\uff0c\u8d73\u8d73\u6025\u884c\uff0c\u5e38\u5984\u5ff5\u3002\u4e00\u5e74\u524d\uff0c\u6005\u7136\u82e5\u5931\u3002\u6b64\u591c\uff0c\u9759\u540c\u53bb\u5e74\uff0c\u5ffd\u839e\u5c14\uff0c\u7136\uff0c\u5954\u96f7\u82e5\u6709\u6240\u5f97\uff0c\u5df2\u7136\u6628\u65e5\u4eca\u65e5\u65e9\u901d\uff0c\u91ca\u7136\u8001\u77e3\u3002'

wfile('utf8',content.encode('UTF-8'))
rfile('utf8')

CODEC = 'UTF-8'
FILE = 'UTF8.FILE'

try:
    fobj = open(FILE, 'w')
except IOError, e:
    print 'error:', e
else:
    fobj.write(content.encode(CODEC))
finally:
    fobj.close() 