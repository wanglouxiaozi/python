#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

users = {
	'A':{
	'first':'yu',
	'last':'lei',
	'location':'hs'
	},
	
	'B':{
	'first':'liu',
	'last':'wei',
	'location':'hs'
	}
}

# username userinfo 相当于key,value
for username, userinfo in users.items():
	print("username:"+username)
	print("userinfo"+str(userinfo))
	fullname = userinfo['first'] + userinfo['last']
	print("fullname:" + fullname)
	print("location:" + userinfo['location'])
