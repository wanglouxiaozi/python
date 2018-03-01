#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

dict = {'runoob': '菜鸟教程', 'google': 'Google搜索'}

print "Value : %s" % dict.setdefault('runoob', None)
print "Value : %s" % dict.setdefault('Taobao', '淘宝')
print "Value : %s" % dict.setdefault('Tianmao', None)
