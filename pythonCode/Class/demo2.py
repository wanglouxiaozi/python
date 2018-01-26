#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

class T:
	num    = 8
	_num1  = 9
	__num2 = 10
	def __init__(self):
		pass
	def getNum(self):
		print T.num
		print T._num1
		print T.__num2

class M(T):
	def __init__(self):
		pass
	
	def fun(self):
		print T._num1

class W:
	def __init__(self):
		pass
	
	def func(self):
		print T._num1


m1 = M()
m1.getNum()
m1.fun()

w1 = W()
w1.func()

print "="*100
print m1.num
print m1._num1
#print m1.__num2 #报错


