#!/usr/bin/python
#Filename: using_cPickle.py

import cPickle as p
#import pickle as p

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

f = file(shoplistfile, 'w')
p.dump(shoplist, f)
f.close()

del shoplist

f = file(shoplistfile)
storedlist = p.load(f)
print storedlist
