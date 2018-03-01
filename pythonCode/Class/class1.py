#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

class Test:
	'这是一个测试例子'
	def prt(self):
		print(self)
		print(self.__class__)
		print(Test.__doc__)

t = Test()
t.prt()
