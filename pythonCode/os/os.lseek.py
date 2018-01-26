#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os, sys

fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
os.write(fd, "This is a test!")

#所有 fsync() 方法
os.fsync(fd)

#从开始位置读取字符串
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print "Read string is: %s" % str

#从位置11读取字符串
os.lseek(fd, 10, os.SEEK_SET)
str = os.read(fd, 100)
print "Read string is:", str

os.close(fd)
print "文件关闭成功"
