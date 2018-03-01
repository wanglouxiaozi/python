#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import copy
a = {1: [1,2,3]}
c = copy.deepcopy(a)
print a, c

a[1].append(4)
print a, c

