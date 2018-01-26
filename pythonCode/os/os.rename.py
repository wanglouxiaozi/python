#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os, sys

path = "test"
try:
	os.mkdir(path, 0755)
	print "test目录成功创建"
except BaseException, Argument:
	print "test目录创建失败 %s" % str(Argument)

print "目录为: %s" % os.listdir(os.getcwd())

try:
	os.rename("test", "test2")
	print "重命名成功！"
	print "重命名后的目录为: %s" % os.listdir(os.getcwd())
	os.removedirs("test2")
	print "test2目录已删除"

except BaseException, Argument:
	print "重命名失败: %s" % str(Argument)


