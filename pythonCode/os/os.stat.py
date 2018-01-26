#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os, sys

with open("a2.py", "w+") as fp:
	pass

#显示文件"a2.py"信息
statinfo = os.stat("a2.py")
print statinfo
