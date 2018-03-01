#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os, sys

fd = os.open("f1.txt", os.O_RDWR|os.O_CREAT)
ret = os.write(fd, "This is runoob.com site\n")
print "写入位数: %d" % ret
os.close(fd)
print "文件关闭成功"
