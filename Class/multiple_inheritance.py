#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

class A:
	def foo(self):
		print ("called A.foo()")

class B(A):
	pass

class C(A):
	def foo(self):
		print("called C.foo()")

#继承object会调用C类的foo,否则会调用A的。使用super进行父类构造调用那么必须使用object继承的新式类，否则报错
class D(B, C, object): 
	pass

if __name__ == "__main__":
	d = D()
	d.foo()
