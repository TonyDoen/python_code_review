#!/usr/bin/python
#Filename: using_str_methods.py

name = 'swaroop'

if name.startswith('swa'):
    print 'yes, the string starts with "swa"'

if 'a' in name:
    print 'yes, it contains the string "a"'

if name.find('war') != -1:
    print 'yes, it contains the string "war"'

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)

test = '||'
print test.join(mylist)
