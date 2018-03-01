#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import os
import sys

FILE = sys.argv[1]
if not FILE.endswith(".hex"):
	print "文件格式不正确"
else:
	print "文件格式正确"


