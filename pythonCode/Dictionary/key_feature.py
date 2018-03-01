#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

#1、不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住

dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print "dict['Name']: ", dict['Name']


#2、键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行。

dict = {['Name']: 'Zara', 'Age': 7}
#print "dict['Name']: ", dict['Name']
#print dict[['Name']]
