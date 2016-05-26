#!/usr/bin/python
#Filename: using_seq.py

shoplist = ['apple', 'mango', 'carrot', 'banana']

for i in range(0, len(shoplist)):
    print 'Item %d is %s' % (i, shoplist[i])

for item in shoplist:
    print 'got %s' % item

for i in range(0, len(shoplist)):
	print 'Item %d is %s' % (-i, shoplist[-i])

print 'Item 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1]
print 'Item start to end is', shoplist[:]

name = 'swaroop'
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:]

for i in name:
    print 'name:', i
