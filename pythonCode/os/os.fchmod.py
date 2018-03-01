#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os, sys, stat

fd = os.open("/tmp/foo.txt", os.O_RDONLY)

#设置文件可通过组执行
os.fchmod( fd, stat.S_IXGRP)

#设置文件可被其他用户写入
os.fchmod( fd, stat.S_IWOTH)

print "修改权限成功！"

os.close(fd)
