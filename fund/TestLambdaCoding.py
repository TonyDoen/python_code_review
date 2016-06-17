# -*- coding:utf8 -*-

def true(): return True # python single line function can be written like this.

def add(x, y): return x+y # lambda x, y: x+y
def normadd(x, y=2): return x+y # lambda x, y=2: x+y
def nousualadd(*z): return z # lambda *z:z

# lambda 这种语句的目的是由于性能的原因,在调用时绕过函数的栈分配。。lambda 表达式运作起来就像一个函数,当被调用时,创建一个框架对象。
ladd = lambda x, y: x+y
lnormadd = lambda x, y=2: x+y
lnousualadd = lambda *z:z

if __name__ == '__main__':
	print add(1,1)
	print normadd(1,1)
	print normadd(1)
	print nousualadd(1, 2, 3)

	# 
	print '-'*30	
	print ladd(1,1)
	print lnormadd(1,1)
	print lnormadd(1)
	print lnousualadd(1, 2, 3)

	
