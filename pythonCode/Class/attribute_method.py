#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

class JustCounter:
	__secretCount = 0 	#私有变量
	publicCount = 0   	#公开变量
	_protectedCount = 0 #受保护变量
	
	def count(self):
		self.__secretCount  += 1
		self.publicCount    += 1
		self._protectedCount += 1
		print 'secretCount: ', self.__secretCount
		print 'protectCount: ', self._protectedCount

counter = JustCounter()
counter.count()
counter.count()
print 'publicCount: ', counter.publicCount
print 'protectedCount: ', counter._protectedCount

#print counter.__secretCount #报错，实例不能访问私有变量

#python 不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性
print counter._JustCounter__secretCount
print "="*100

count = JustCounter()
#print count.__secretCount
print 'protectedCount: ', count._protectedCount
print "publicCount: ", count.publicCount
count.count()
print "publicCount: ", count.publicCount
