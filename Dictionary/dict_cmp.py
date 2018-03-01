#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Name': 'Mahnaz', 'Age': 27}
dict3 = {'Name': 'Abid', 'Age': 27}
dict4 = {'Name': 'Zara', 'Age': 7}
dict5 = {'Name': 'a', 'Age': 7}
print "Return value: %d" % cmp (dict1, dict2)
print "Return value: %d" % cmp (dict2, dict3)
print "Return value: %d" % cmp (dict1, dict4)
print "Return value: %d" % cmp (dict4, dict5)
print "=" * 100


#字典cmp()的比较规则：
#先比较字典的长度，如果相等。再比较adiff(在A中与B值不相等的最小key)和bdiff(在B中与A值不相等的最小key),再等则比较两者的值。
#长度相等，直接比较'Addr' 和 'Adds', 所以dict6 < dict7:
dict6 = {'Name': 'e', 'Age': 30, 'Addr': 'hust'}
dict7 = {'Name': 'z', 'Age': 30, 'Adds': 'hust'}
print "Return Value: %d" % cmp (dict6, dict7)


#长度相等， key完全相等, 比较value不等keys('Name', 'Age', 'Addr')中的最小key('Addr')的value ('hust', 'whu'),所以dict8 < dict9
dict8 = {'Name': 'e', 'Age': 30, 'Addr': 'hust'}
dict9 = {'Name': 'z', 'Age': 27, 'Addr': 'whu'}
print "Return Value: %d" % cmp (dict8, dict9)
