#!/usr/bin/python
#Filename: using_class_objvar.py

class Person:
	'''represent a person.'''
	population = 0
	
	def __init__(self, name):
		'''initializes the person's data.'''
		self.name = name
		print '(initializing %s)' % self.name

		Person.population += 1

	def __del__(self):
		'''i am dying.'''
		print '%s says bye.' % self.name

		Person.population -= 1
	    
		if Person.population == 0:
		    print 'i am the last one.'
		else:
		    print 'there are still %d people left.' % Person.population

	def sayHi(self):
		'''greeting by the person'''
		print 'hi, my name is %s.' % self.name

	def howMany(self):
		'''prints the current population.'''
		if Person.population == 1:
		    print 'i am the only person here.'
		else:
		    print 'we have %d persons here.' % Person.population

tony = Person('tony')
tony.sayHi()
tony.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

tony.sayHi()
tony.howMany()

