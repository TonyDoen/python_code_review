# -*- coding:utf8 -*-

'''
create text file
'''

import os

ls = os.linesep

#get filename
while True:
	filename = raw_input('>')
	if os.path.exists(filename):
		print 'error: %s already exists' % filename
	else:
		break

print '\nenter lines (. by itself to quit)\n'

all = []
while True:
	entry = raw_input('>')
	if '.' == entry:
		break
	else:
		all.append(entry)

fobj = open(filename, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print 'done.'