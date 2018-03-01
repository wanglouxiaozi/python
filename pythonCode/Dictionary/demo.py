#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

def test(dict1, list1):
	dict1.pop('name')
	list1.pop()
	print dict1, list1

def test2(str1):
	str1 = 's'
	print str1

def __main():
	dict1 = {'name': 'allen', 'age': 24, 'sex': 'm'}
	list1 = ['nihao', 'shanghai']
	print dict1, list1
	test(dict1, list1)
	print dict1, list1
	
	str1 = "hello world"
	print str1
	test2(str1)
	print str1
if __name__ == '__main__':
	__main()
	
