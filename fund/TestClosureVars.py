# -*- coding:utf8 -*-

w = x = y = z = 1
def printwxyz():
	output = '<int %r id=%#0x val=%d>'
	print output % ('w', id(w), w)
	print output % ('x', id(x), x)
	print output % ('y', id(y), y)
	print output % ('z', id(z), z)


def f1():
	x = y = z = 2
	def f2():
		y = z = 3
		print '\nin f2:'
		printwxyz()
	f2()
	print '\nin f1:'
	printwxyz()

def f3():
	z = 4
	print '\nin f3:'
	printwxyz()

printwxyz()

# clo = f3.func_closure
# if clo:
# 	print "f3 closure vars:", [str(c) for c in clo]
# else:
# 	print "no f3 closure vars"

# f3()
# clo = f2.func_closure
# if clo:
# 	print "f2 closure vars:", [str(c) for c in clo]
# else:
# 	print "no f2 closure vars"

# f2()
clo = f1.func_closure
print clo
if clo:
	print "f1 closure vars:", [str(c) for c in clo]
else:
	print "no f1 closure vars"

f1()
