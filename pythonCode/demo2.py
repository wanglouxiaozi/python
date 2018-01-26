#!/usr/bin/env python2

import im1
import demo1
from demo1 import test

def testt():
	im1.hello()
	demo1.test()
	test()

def __main():
	testt()

if __name__ == "__main__":
	__main()
