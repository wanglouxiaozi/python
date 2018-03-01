#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

people = {
	'A': {
		'first' : 'allen',
		'last' : 'wang',
		'age' : 25
	},
	'B': {
		'first' : 'jack',
		"last" : 'wu',
		'age' : 0, 
	}
}

print people['A']['age']
print people['B']['last']
print people['B']["last"]
people['B']['last'] = "wang"
print people['B']['last']
print people['B']['age']


user = {}
user['A'] = {'first' : "allen", 'last':"wang" ,}
print user
user['B'] = {'first' : "gailun", 'last': "yingxiong"}
print user


for usr in user.items():
	print usr
