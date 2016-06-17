# -*- coding:utf8 -*-	

def fun_var_args_call(arg1, arg2, arg3):
	print "arg1:", arg1  
	print "arg2:", arg2  
	print "arg3:", arg3 

def fun_var_args_star(farg, *args):
	print 'arg:', farg
	for value in args:
		print 'second arg:', value # *args 当作可容纳多个变量组成的list 

def fun_var_args_2star(farg, **kwargs):
	print 'arg:', farg
	for key in kwargs:
		print 'second arg: %s:%s' % (key, kwargs[key]) # myarg2和myarg3被视为key， 感觉**kwargs可以当作容纳多个key和value的dictionary 	

def testit(func, *nkwargs, **kwargs): #this is we want to test it
	try:
		retval = func(*nkwargs, **kwargs)
		result = (True, retval)
	except Exception, diag:
		result = (False, str(diag))
	return result

def test():
	funcs = (int, long, float)
	vals = (1234, 12.34, '1234', '12.34')
	for eachfunc in funcs:
		print '-'*20
		for eachval in vals:
			retval = testit(eachfunc, eachval)
			if retval[0]:
				print '%s(%s)' % (eachfunc.__name__, `eachval`), retval[1]
			else:
				print '%s(%s) = FAILED:' % (eachfunc.__name__, `eachval`), retval[1]

if __name__ == '__main__':
	test()
	print '-'*20
	fun_var_args_star(1,'two',3)
	fun_var_args_2star(farg=1, myarg2='two', myarg3=3)

	args = ["two", 3] #list 
	kwargs = {"arg3": 3, "arg2": "two"} # dictionary
	fun_var_args_call(1, *args)
	fun_var_args_call(1, **kwargs)