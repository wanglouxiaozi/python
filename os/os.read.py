#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os, sys
fd = os.open("f1.txt", os.O_RDWR)

ret = os.read(fd, 15)
print ret

os.close(fd)
print "关闭文件成功"
