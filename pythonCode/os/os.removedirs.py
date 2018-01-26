#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os, sys 

def test():
	try:
		#列出目录
		print "目录为: %s" % os.listdir(os.getcwd())

		#移除
		os.removedirs("test")
	
		#列出移除后的目录
		print "移除后目录为: %s" % os.listdir(os.getcwd())
	except BaseException, Argument:
		print "[Catch Error]%s" % str(Argument)

def __main():
	test()

if __name__ == "__main__":
	__main()
