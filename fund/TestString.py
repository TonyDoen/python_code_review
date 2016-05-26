# -*- coding:utf8 -*-

import string

alphas = string.letters + '_'
num = string.digits

print alphas, num

from string import Template
s = Template('There are ${hm} ${la} Quotation Symbols')
print s.safe_substitute(lang='python')
print s.safe_substitute(la='python')
print s.safe_substitute(hm='3', la='python')
print s.substitute(hm='3', la='python')

print '%d' % 10
print '%x' % 10
print '%#x' % 10
print '%X' % 10
print '%#X' % 10

print '%f' % 10.111111111
print '%3.3f' % 10.111111111
print '%E' % 10.111111111

print '%d%%' % 10

import re
m = re.search(r'\\[rtfvn]', r'hello world\n')
if m is not None:
    print m.group()

#内建函数
print cmp('aaa','aaa')
print cmp('aaa','bbb')
print cmp('bbb','aaa')

print len('aaa')
print max('abc')
print min('abc')

for i, t in enumerate('abcdefghijklmnopqrstuvwxyz'):
    print i, t

s, t = 'flin', 'oxyz'
print zip(s,t)

print u'abc'
print u'\u8320'
print isinstance(u'', basestring)

print chr(65)
print unichr(65)
print ord('A')
print ord(u'\u8320')

print r'\r', '\r'                         #回车
print r'\t', '\t'                         #横向制表符
print r'\f', '\f'                         #换页
print r'\v', '\v'                         #纵向制表符
print r'\n', '\n'                         #换行
print r'\0', '\0'                         #空字符
print r'\a', '\a'                         #响铃字符
print r'\b', '\b'                         #退格
print r'\n', '\n'                         #换行

src = '''here, i want to show some string intern function.\ni am
         boy
      '''

print src.capitalize()                    #首字母大写
print src.center(100)                     #指定字符数居中
print len(src.center(100))

print src.count('s', 0, 17)               #指定范围 str 出现的次数
print src.endswith('.', 0, len(src))      #指定范围内 str 为结束符
print src.find('s',0,len(src))            ##查找指定范围 str 开始的索引值，没有返回-1
print src.rfind('s',0,len(src))  
print src.index('s',0,len(src))           #查找指定范围 str 开始的索引值，没有抛异常
print src.rindex('s',0,len(src))
print src.isalnum()                       #src至少有一个字符，且所有字符是 字母或者数字
print ('aaa').isalnum()
print ('袈袉').isalnum()
print ('aaaa').isalpha()                  #src至少有一个字符，且所有字符是 字母
#print ('178793').isdecimal()              #src至少有一个字符，且所有字符是数字
print src.isdigit()                       #src至少有一个字符，且所有字符是数字
print src.islower()                       #src至少有一个区分大小写的字符，且所有字符是小写
#print src.isnumeric()                     
print src.isspace()
print src.istitle()
print src.isupper()
print src.join('abc')
print src.ljust(100)                      #左对齐
print src.rjust(100)
print src.lower()
print src.upper()
print src.swapcase()                      #翻转大小写
print src.strip()
print src.lstrip()                        #截掉左边的空格
print src.rstrip()
print src.partition('o')                  #把字符串 src 从 str 出现的第一个位置起 分为3个元素的元组
print src.rpartition('o')
print src.replace('o','h',2)              #把 'o' 替换成 'h' 指定次数 2次
print src.split(' ',src.count(' '))
print src.split(' ')
print src.splitlines(src.count('\n'))
print src.splitlines()
print src.startswith('h',0,len(src))
print src.title()
# print src.translate()
print src.zfill(100)                      #返回长度 为 100 的字符串，原字符串右对齐前填充 0 


print ('8320').decode(encoding='UTF-8', errors='strict')#errors=strict/ignore/replace
print ('袈袉').decode(encoding='UTF-8', errors='strict')
print ('8888').encode(encoding='UTF-8', errors='strict')
print (u'\u8888\u8889').encode(encoding='UTF-8', errors='strict')
