#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

a = {1: [1,2,3]}
b = a.copy()
print a, b

a[1].append(4)
print a, b
