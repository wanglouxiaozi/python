#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os, sys

fd = os.open("foo.txt", os.O_RDWR|os.O_CREAT)

#复制文件描述符
d_fd = os.dup(fd)

os.write(d_fd, "hello,This is a test!!\n")

#关闭文件（关闭该文件所有的文件描述符）
os.closerange(fd, d_fd)

print "关闭所有文件成功！"

