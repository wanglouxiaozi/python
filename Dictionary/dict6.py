#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

seq = ('name', 'age', 'sex')
dict1 = {}
dict1 = dict1.fromkeys(seq)
print "New Dictionary : %s" % str(dict1)

dict2 = {}
dict2 = dict2.fromkeys(seq, 30)
print "New Dictionary: %s" % str(dict2)

dict = dict.fromkeys(seq)
print "New Dictionary: %s" % str(dict)
