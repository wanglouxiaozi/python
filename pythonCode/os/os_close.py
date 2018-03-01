#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os, sys

#打开文件
fd = os.open("foo.txt", os.O_RDWR|os.O_CREAT)

#写入字符串
os.write(fd, "This is a test!\n")

#关闭文件
os.close(fd)

print "文件关闭成功!!"
