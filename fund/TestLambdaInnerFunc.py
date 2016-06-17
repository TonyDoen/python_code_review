# -*- coding:utf8 -*-
# apply(), filter(), map(), reduce()
# apply(func[, nkw][, kw])  # 用可选的参数来调用func, nkw 为非关键字参数, kw 关键字参数; 返回值是函数调用的返回值。python1.6 中有效的摈弃了 apply()。
# filter(func, seq)         # 调用一个布尔函数func 来迭代遍历每个 seq 中的元素; 返回一个使 func 返回值为 ture 的元素的序列。
# map(func, seq1[,seq2...]) # 将函数func 作用于给定序列(s)的每个元素, 并用一个列表来提供返回值; 如果func 为 None, func 表现为一个身份函数,返回一个含有每个序列中元素集合的 n 个元组的列表。
# reduce(func, seq[, init]) # 将二元函数作用于 seq 序列的元素, 每次携带一对(先前的结果以及下一个序列元素),连续的将现有的结果和下雨给值作用在获得的随后的结果上,最后减少我们的序列为一个单一的返回值;如果初始值 init 给定,第一个比较会是 init 和第一个序列元素而不是序列的头两个元素。

def odd(n):
	return n % 2

def fake_filter(bool_func, seq):
	filtered_seq = []
	for each in seq:
		if bool_func(each):
			filtered_seq.append(each)
	return filtered_seq

def fake_map(func, seq):
	mapped_seq = []
	for each in seq:
		mapped_seq.append(func(each))
	return mapped_seq

# def fake_reduce(func, seq):
# 	if init is None:
# 		res = seq.pop(0)
# 	else:
# 		res = init
# 		for each in seq:
# 			res = func(res, each)
# 	return res

if __name__ == '__main__':
	randomNums = []
	from random import randint
	for each in range(9):
		randomNums.append(randint(1, 99))
	print randomNums, '\n', filter(odd, randomNums), '\n', fake_filter(odd, randomNums)
	print [n for n in randomNums if n%2]

	# 
	print [n for n in [randint(1, 99) for each in range(9)] if n%2] # equal 19-23 line 

	# randomNums.append(n for n in )
	print [randint(1, 99) for each in range(9)]
	print [n for n in [randint(1, 99) for each in range(9)]]
	print randomNums.extend([n for n in [randint(1, 99) for each in range(9)]])
	print randomNums

	# 
	print map((lambda x:x+2),[0,1,2,3,4,5])
	print [x+2 for x in [0,1,2,3,4,5]]

	print map((lambda x:x**2), [0,1,2,3,4,5])
	print [x**2 for x in [0,1,2,3,4,5]]

	print map(lambda x, y: x+y, [0, 1, 2, 3], [4, 5, 6, 7])
	print map(lambda x, y: (x-y, x+y, x*y, x**y), [0, 1, 2, 3], [4, 5, 6, 7])
	print map(None, [0, 1, 2, 3], [4, 5, 6, 7])
	print zip([0, 1, 2, 3], [4, 5, 6, 7])

	# how to feel reduce, reduce(func, [0, 1, 2, 3, 4]) = func(func(func(func(0, 1), 2), 3), 4)
	def sum(x, y): return x + y
	def time(x, y): return x * y
	total = 0 # init
	for each in range(9):
		total = sum(total, each) # reduce
	print total # return result

	print reduce(sum, range(9)) # equal 63-67 line.
	print reduce(time, range(9)[1:])
	print range(9)[1:]
	print filter(lambda x:x>0, range(9))

	print reduce(lambda x, y: x+y, 'hello world')
	# print fake_reduce(lambda x, y: x+y, 'hello world')
	
	# 偏函数应用:currying 的概念将函数式编程的概念和默认参数以及可变参数结合在一起。。一个带 n 个参数,curried 的函数固化第一个参数为固定参数,并返回另一个带 n-1 个参数函数对象,分别类似于 LISP的原始函数 car 和 cdr 的行为。
	#          Currying 能泛化成为偏函数应用(PFA), 这种函数将任意数量(顺序)的参数的函数转化成另一个带剩余参数的函数对象。
	#          当调用带许多参数的函数的时候,PFAs 是最好的方法。

	from operator import add, mul # equal sum, time above
	from functools import partial
	add1 = partial(add, 1) # add1(x) == add(1, x)
	mul100 = partial(mul, 100) # mul100(x) == mul(100, x)
	print add(1, 5), add1(5)
	print mul(100, 3), mul100(3)

	# 
	base2 = partial(int, base=2) # 使用int()内建函数并将 base 固定为 2 来指定二进制字符串转化。
	base2.__doc__ = 'Convert base 2 string to an int.'
	print base2('00001010')

	base2fucked = partial(int, 2)
	print int('0011', 2), #base2fucked('0011') #error 为固定参数的总是放在运行时刻参数的左边,关键字参数总是出现在由于关形参之后, base=2

	# 
	import Tkinter
	root = Tkinter.Tk()
	Mbtn = partial(Tkinter.Button, root, fg='white', bg='blue')
	b1 = Mbtn(text='button 1')
	b2 = Mbtn(text='button 2')
	qb = Mbtn(text='quit', bg='red', command=root.quit)
	b1.pack()
	b2.pack()
	qb.pack(fill=Tkinter.X, expand=True)
	root.title('PFAs.')
	root.mainloop()
	pass




