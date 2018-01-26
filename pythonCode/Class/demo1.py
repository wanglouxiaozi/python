#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

class T:
	num = 0	
	_num = 10

class M:
	__num2 = 0
	__num3 = 0
	def count(self):
		T.num += 1
		print T.num
	def getCount(self):
		__num2 = T.num
		print __num2
		__num3 = T._num
		print __num3

class W:
	def count(self):
		T.num += 1
		print T.num
	
	def getCount(self):
		print T.num		

m1 = M()
m1.count()
w1 = W()
w1.count()
m1.getCount()
