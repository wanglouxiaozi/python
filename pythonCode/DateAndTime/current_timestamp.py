#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import time #引入time模块

ticks = time.time()
print "="*100
print "当前时间戳为:", ticks
print "="*100



#获取当前时间
localtime = time.localtime(time.time())
print "本地时间为:", localtime
print "="*100



#获取格式化的时间
localtime = time.asctime(time.localtime(time.time()))
print "本地时间为:", localtime
print "="*100



#格式化日期
#可以使用time模块的strftime方法来格式化日期 time.strftime(format[, t])

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

#格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

#将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
print "="*100



#获取某月日历
import calendar

cal = calendar.month(2018, 1)
print "以下输出2018年1月份的日历:"
print cal
print "="*100
