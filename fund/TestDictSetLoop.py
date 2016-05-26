# -*- coding:utf8 -*-

'''using dict
'''
number = {1:'one',2:'two',3:['three1',['three2.1','three2.2','three2.3']]}
print number
print number.has_key(1)
print number.get(1)
print number.items()
print number.keys()
print number.values()

num1 = number.copy()
num2 = dict.fromkeys((1,2,3,4,5,6),['one','two','three'])
print num1
print num2
print num2.pop(1), '\n', num2
print num2.setdefault(1), '\n', num2
print num2.update(num1), '\n', num2

print number.clear()
print number, num1

# Set
s1 = set(num1.keys())
s2 = set('abcddddddddddefg')
fs = frozenset(num1)
print s1, s2, fs
print 'a' in s2
print 'a' not in s2

print s2.copy()
print s2.issubset(s1)
print s2.issuperset(s1)
print s2.union(s1)
print s2.intersection(s1)
print s2.difference(s1)
print s2.symmetric_difference(s1)

print s2.update('x'), s2                                  #交集
print s2.intersection_update('x'), s2                     #并集
print s2.difference_update(set('abc')), s2                #差集
print s2.symmetric_difference_update(set('abcdef')), s2   #xor
print s2.add('y'), s2
print s2.remove('a'), s2
print s2.discard('z'), s2
print s2.pop(), s2

print s1 | set('456')
print fs | set('456')
print s1 & fs
print s1 & set('345')
print s1 - fs
print s1 - set('345')
print s1 ^ fs
print s1 ^ set('345')

s1 |= set('123')
print s1

s2 &= set('abc')
print s2

s1 -= set('234')
print s1

s1 ^= set([2,3,4])
print s1

#if expression:
#elif expression:
#else:

#for while
while True:
    break

count = 1
while count < 9:
    print count,
    count += 1
print

for var in range(10):
    print var,
print

for var in 'agree':
    print var,
print

namel = ['tony1','tony2','tony3','tony4','tony5']
for i in range(len(namel)):
    print i, namel[i],
print

for i, na in enumerate(namel):
    print '%d %s' % (i, na),
print

i = iter(namel)
while True:
    try:
        print i.next(),
    except StopIteration:
        break
print

#列表解析
print [x**2 for x in xrange(6)]
print [(x+1,y+1) for x in xrange(3) for y in xrange(5)] 

#生成器表达式
line = '''aaa aaaa aaaaaaa aaaaaaaaa aaaaa aaaa aaa aaaa aaaaa aaaaa  aaaaaaaa aaaaa aa
aaa aaaa aaaaaaa aaaaaaaaa aaaaa aaaa aaa aaaa aaaaa aaaaa  aaaaaaaa aaaaa aa bb, cc dd
aaa aaaa aaaaaaa aaaaaaaaa aaaaa aaaa aaa aaaa aaaaa aaaaa  aaaaaaaa aaaaa aa bb, cc dd
aaa aaaa aaaaaaa aaaaaaaaa aaaaa aaaa aaa aaaa aaaaa aaaaa  aaaaaaaa aaaaa aa bb, cc dd
aaa aaaa aaaaaaa aaaaaaaaa aaaaa aaaa aaa aaaa aaaaa aaaaa  aaaaaaaa aaaaa aa bb, cc dd
'''
print sum(len(word) for ln in line for word in ln.split())

rows = [1,2,3,4]
def cols():
    yield 9
    yield 8
    yield 7

xpair = ((i, j) for i in rows for j in cols())
for pr in xpair:
    print pr

#old read
f = open('/etc/passwd', 'r')
longest = 0
while True:
    linelen = len(f.readline().strip())
    if not linelen:
        break
    if linelen > longest:
        longest = linelen
f.close()
print longest

#older read
f = open('/etc/passwd', 'r')
longest = 0
alllines = f.readlines()
f.close()
for line in alllines:
    linelen = len(line.strip())
    if linelen > longest:
        longest = linelen
print longest

#imp read
f = open('/etc/passwd', 'r')
longest = 0
alllines = [x.strip() for x in f.readlines()]
f.close()
for line in alllines:
    linelen = len(line)
    if linelen > longest:
        longest = linelen
print longest

#fresh read
f = open('/etc/passwd', 'r')
alllines = [len(x.strip()) for x in f]
f.close()
print max(alllines)

f = open('/etc/passwd', 'r')
longest = max(len(x.strip()) for x in f)
f.close()
print longest

print max(len(x.strip()) for x in open('/etc/passwd', 'r'))

for line in open('/etc/passwd','r'):
    print line, 

f = open('/etc/passwd', 'r')
for line in f:
    print line,

print 'start.'
print f.fileno()
print f.flush()
print f.isatty()
print f.read(-1)
# print f.readinto()
print f.readline(3)
print f.readlines(100) 
f.close()
print 'end.'

import os
print 'os.linesep', os.linesep #文件 行分隔符
print 'os.sep', os.sep         #文件 路径名的分隔符
print 'os.pathsep', os.pathsep #文件 路径的分隔符
print 'os.curdir', os.curdir   #当前工作目录的字符串名称
print 'os.pardir', os.pardir   #当前工作目录父目录的字符串名称

print os.path.isdir('/tmp')
print os.chdir('/tmp')
print os.getcwd()
