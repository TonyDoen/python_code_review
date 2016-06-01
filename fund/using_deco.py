# -*- coding:utf8 -*-
''' a example for using deco '''

from time import ctime, sleep

def tsfunc(func):
	def wrappedfunc():
		print '[%s] %s() called' % (ctime(), func.__name__)
		return func()

	return wrappedfunc

@tsfunc
def foo():
	pass

foo()
sleep(4)

for i in range(2):
	sleep(1)
	foo()
	