#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os, sys

path = "/dev/fb0"

#获取元组
info = os.lstat(path)

#获取 major 和 minor 设备号
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)

print "Major 设备号 :", major_dnum
print "Minor 设备号 :", minor_dnum
