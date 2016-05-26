#!/usr/bin/python
#Filename: using_class_inherit.py

class SchoolMember:
	'''represents any school member.'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
#	    print '(initialized SchoolMember: "%s")' % self.name
	
	def tell(self):
		'''tell my details'''
		print 'name: "%s", age: "%s"' % (self.name, self.age)

class Teacher(SchoolMember):
	'''represents a teacher.'''
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print '(initialized teacher: %s)' % self.name

	def tell(self):
		SchoolMember.tell(self)
		print 'salary: "%d"' % self.salary

class Student(SchoolMember):
	'''represents a student.'''
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print '(initialized student: %s)' % self.name
	
	def tell(self):
		SchoolMember.tell(self)
		print 'marks: "%d"' % self.marks


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Tony', 22, 75)
print

members = [t, s]
for mem in members:
    mem.tell()

		
