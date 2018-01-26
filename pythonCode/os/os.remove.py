#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os, sys 

def test():
	#列出目录
	print "目录为: %s" % os.listdir(os.getcwd())

	#移除
	try:
		os.remove("aa.txt")
		os.remove("folder")
	except OSError, Argument:
		print "%s" % str(Argument)

	#移除后列出目录
	print "移除后: %s" % os.listdir(os.getcwd())

def __main():
	test()

if __name__ == "__main__":
	__main()
