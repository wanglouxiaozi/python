#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
'''
return 语句

return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。之前的例子都没有示范如何返回数值，下例便告诉你怎么做：
'''


#可写函数说明
def sum(arg1, arg2):
	#返回林格该参数的和
	total = arg1 + arg2
	print "函数内: ", total
	return total

#调用sum函数
total = sum(10, 20)
print "函数外: ", total
