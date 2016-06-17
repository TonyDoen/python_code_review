# -*- coding:utf8 -*-

bar = 100
this_is_global = 'xzy'
def foo():
	print '\ncalling foo()...'
	bar = 200
	# bar vs. this_is_global
	global this_is_global
	this_is_global = 'new define'
	print 'in foo(), bar is %d and this_is_global now is %s' % (bar, this_is_global)

def outer():
	m = 3
	def inner():
		n = 4
		print m, n, m+n
	print m, inner()

def counter(start=0):
	count = [start]
	def incr():
		count[0] += 1
		return count[0]
	return incr()

if __name__ == '__main__':
	print 'in __main__, bar is %d and this_is_global is %s' % (bar, this_is_global)
	foo()
	print '\nin __main__, bar is %d and this_is_global is %s' % (bar, this_is_global)

	outer()

	print '\n', counter, counter(3)