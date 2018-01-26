#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

#Python 字典(Dictionary) fromkeys()函数用于创建一个新字典， 以序列seq中元素做字典的键,value为字典所有键对应的初始值。

seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print "New Dictionary: %s" % str(dict)

dict = dict.fromkeys(seq, 10)
print "New Dictionary: %s" % str(dict)
