# -*- coding:utf8 -*-
# 
def fab1(max): # 直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差
    n, a, b = 0, 0, 1 
    while n < max: 
        print b 
        a, b = b, a + b 
        n = n + 1

def fab2(max): # 返回一个 List, 该函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，最好不要用 List
    n, a, b = 0, 0, 1 
    L = [] 
    while n < max: 
        L.append(b) 
        a, b = b, a + b 
        n = n + 1 
    return L

# 通过 iterable 对象来迭代
# for i in range(1000): pass

# 会导致生成一个 1000 个元素的 List，而代码：
# for i in xrange(1000): pass
# 不会生成一个 1000 个元素的 List，而是在每次迭代中返回下一个数值，内存空间占用很小。因为 xrange 不返回 List，而是返回一个 iterable 对象。

class Fab3(object): 
    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 

    def __iter__(self): 
        return self 

    def next(self): # Fab 类通过 next() 不断返回数列的下一个数，内存占用始终为常数
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()

def fab4(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b # 保持第一版 fab 函数的简洁性，同时又要获得 iterable 的效果，yield 就派上用场
        # print b 
        a, b = b, a + b 
        n = n + 1 
# 简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。
# 在一个 generator function 中，如果没有 return，则默认执行至函数完毕，如果在执行过程中 return，则直接抛出 StopIteration 终止迭代。
def read_file(fpath): # 一个 yield 的例子来源于文件读取。如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用。好的方法是利用固定长度的缓冲区来不断读取文件内容。通过 yield，我们不再需要编写读文件的迭代类，就可以轻松实现文件读取
	BLOCK_SIZE = 1024
	with open(fpath, 'rb') as f:
		while True:
			block = f.read(BLOCK_SIZE)
			if block:
				yield block
			else:
				return

if __name__ == '__main__':
	fab1(5)
	print [n for n in fab2(5)], fab2(5),
	print [n for n in Fab3(5)]
	print [n for n in fab4(5)]

	from inspect import isgeneratorfunction # 判断一个函数是否是一个特殊的 generator 函数
	print isgeneratorfunction(fab4)
	print isgeneratorfunction(Fab3)

	import types
	from collections import Iterable
	print isinstance(fab4, types.GeneratorType), isinstance(fab4(5), types.GeneratorType)
	print isinstance(fab4, Iterable), isinstance(fab4(5), Iterable) 
