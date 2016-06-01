# -*- coding:utf8 -*-

import MapReduce, sys

class InvertedIndex:
	def __init__(self):
		self.mr = MapReduce.MapReduce

	def mapper(self, record):
		fileName = record[0]
		value = record[1]
		words = value.split()
		for w in words:
			self.mr.emit_intermediate(w, fileName)

	def reducer(self, key, fileNames):
		fileList = []
		for fileName in fileNames:
			if fileName not in fileList:
				fileList.append(fileName)
		self.mr.emit((key, fileList))

	def execute(self, data):
		self.mr.execute(data, self.mapper, self.reducer)

if __name__ == '__main__':
	data = open(sys.argv[1])
	ii = InvertedIndex()
	ii.execute(data)
	print 'hello'
	#execute(data)


