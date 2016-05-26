# -*- coding:utf8 -*-

'''
read text 
'''

fname = raw_input('enter filename:')
print

try:
	fobj = open(fname, 'r')
except IOError, e:
	print 'error:', e
else:
	for line in fobj:
		print line,
finally:
    fobj.close()
