#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

"""
编写字典程序:

    1. 用户添加单词和定义
    2. 查找这些单词
    3. 如果查不到，请让用户知道
    4. 循环

"""

#创建字典  while开关  字典添加  字典寻找

dictionary = {}
flag = 'a'
pape = 'a'
off = 'a'
while flag == 'a' or 'c' :
	flag = raw_input("添加或查找单词 ?(a/c)")
	if flag == 'a':                                    #开启
		word = raw_input("输入单词(key):")	
		defintion = raw_input("输入定义值(value):")  
		dictionary[str(word)] = str(defintion)         #添加字典
		print "添加 %s 成功" % str(word)
		pape = raw_input("您是否要查找字典? (a/0)")    #read
		if pape == 'a' :
			print dictionary
		else :
			continue
	elif flag == 'c' :
		check_word = raw_input("要查找的单词:")       #检索
		for key in sorted(dictionary.keys()):
			if str(check_word) == key:
				print "该单词存在！", key, dictionary[key]
				off = 'a'
				break
			else :
				off = 'b'
		if off == 'b':
			print "抱歉，%s该值不存在" % str(check_word)
	else:
		print "error type"
		break
