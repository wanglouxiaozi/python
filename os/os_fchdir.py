#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os, sys

#首先到目录"/var/"
os.chdir("/var/")

#输出当前目录
print "当前工作目录为 : %s" % os.getcwd()

#打开新目录
fd = os.open( "/tmp", os.O_RDONLY )

#使用 os.fchdir() 方法修改到新目录
os.fchdir(fd)

#输出当前目录
print "当前工作目录为 : %s" % os.getcwd()

#关闭打开的目录
os.close(fd)
