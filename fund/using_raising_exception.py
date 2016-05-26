#!/usr/bin/python
#Filename:using_raising_exception.py

class ShortInputException(Exception):
#    '''a user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
       

try:
    s = raw_input('enter something --> ')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
except EOFError:
    print '\nwhy did you do an EOF on me?'
except ShortInputException, x:
    print 'ShortInputException: the input was of length %d, was expecting at least %d' % (x.length, x.atleast)
else:
    print 'no exception was raised.'

