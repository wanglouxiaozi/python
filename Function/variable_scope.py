#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

'''
变量作用域

一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里赋值的。
变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。两种最基本的变量作用域如下：

    全局变量
    局部变量

全局变量和局部变量

定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。

局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。如下实例：
'''

total = 0 #这是一个全局变量
#可写函数说明
def sum(arg1, arg2):
	#返回两个参数的和
	total = arg1 + arg2 #total在这里是局部变量
	print "函数内是局部变量: ", total
	return total

def sum2(arg1, arg2):
	global total
	total = arg1 + arg2
	print "函数内是全局变量: ", total
	return total
	

#调用sum函数
sum(10, 20)
sum2(10, 20)
print "函数外是全局变量: ", total

