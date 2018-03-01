#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
#Python字典items()函数以列表返回可遍历的（键，值）元组数组
dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
print "字典值 : %s" % dict.items()

#遍历字典列表
for key,values in dict.items():
	print key,values
