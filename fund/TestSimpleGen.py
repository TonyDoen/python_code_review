# -*- coding:utf8 -*-
# 生成器
def simpleGen():
	yield 1
	yield '2 --> punch'

s = simpleGen()
print s.next()
print s.next()

for each in simpleGen():
	print each

from random import randint
def randGen(ali):
	while len(ali) > 0:
		yield ali.pop() # ali.pop(randint(0, len(ali)))

for each in randGen(['rock', 'paper', 'scissors']):
	print each