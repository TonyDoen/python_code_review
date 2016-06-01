# -*- coding:utf8 -*-

def convert(func, seq):
    """conv. sequence of numbers to same type"""
    return [func(eachnum) for eachnum in seq]

if __name__ == '__main__':
    myseq = (123, 45.67, -6.3, -6.2e8, 99999999L)
    print convert(int, myseq)
    print convert(long, myseq)
    print convert(float, myseq)