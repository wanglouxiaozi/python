#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import re
'''
line = "bababaiijjimmm\n"

matchObj = re.search("ijj", line).span()

print "matchObj.group():", matchObj
'''

line = "<SLOT ID=\"5\" TYPE=\"ETH\" NetworkType=\"\" IP=\"10.12.32.170\" LINK=\"eth0\" INET=\"OK\" PS=\"OK\" "

matchObj = re.search(r'\<SLOT (.*?)=(".*?")', line, re.M|re.I)

print matchObj.group()
print matchObj.group(1)
print matchObj.group(2)


matchObj = re.search(r'IP=(".*?")', line, re.M|re.I)
print matchObj.group()
print matchObj.group(1)


matchObj = re.search(r'INET=(.*?)', line, re.M|re.I)
print matchObj.group()
print matchObj.group(1)
