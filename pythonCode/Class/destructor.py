#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import time

class Point:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
		class_name = self.__class__.__name__
		print class_name, "创建"
	
	
	#析构函数在程序程序退出时自动调用
	def __del__(self):
		class_name = self.__class__.__name__
		print class_name, "销毁"
	def display(self):
		print "x = ", self.x, ", y = ", self.y
'''
pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3) #打印对象的id
del pt1
del pt2
del pt3

time.sleep(10)
'''

pt1 = Point(1, 2)
pt2 = Point(3, 4)
pt1.display()
pt2.display()

#del pt1

time.sleep(3)

