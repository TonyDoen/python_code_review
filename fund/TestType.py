# -*- coding:utf8 -*-

def displaynumtype(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number type:', type(num).__name__
    else:
        print 'not a number type.'

import types
def displaynumtype2(num):
    print num, 'is',
    if type(num) == types.IntType:
        print 'a number type:', type(num).__name__
    else:
        print 'not a number type.'

from types import IntType #减少查询次数
def displaynumtype3(num):
    print num, 'is',
    if type(num) is IntType: #减少值比较 && 减少函数调用次数
        print 'a number type:', type(num).__name__
    else:
        print 'not a number type.'

from decimal import Decimal

displaynumtype('''fff''')
displaynumtype3(None)
displaynumtype2(55)
displaynumtype2(Decimal(55))

print type(55)
print type(type(55))

foo = 'abcdefg'
print foo[::-1]
print foo[::-2]
print foo[::1]
print foo[::2]

x = "hello"
print id(x), x
x = "world"
print id(x), x

s = "abcdefghijklmnopqrstuvwxyz"
for i in [None]+range(-1, -len(s), -1):
    print i, s[0 if i is None else i]
    print i, s[:i]
    print i, s[::i]

arr = [1,2,3,4,5,6,7]
ta = tuple(arr)
print arr, '\n', ta

arr[0] = 66
print arr, '\n', ta

arr = [(1,2),(2,3),(3,4),(4,5),(5,6)]
ta = tuple(arr)
print arr, '\n', ta
arr[0] = (6,6,6,6)
print arr, '\n', ta
