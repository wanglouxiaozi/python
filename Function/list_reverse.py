#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

def reverse(li):
	for i in range(0, len(li)/2):
		temp = li[i]
		li[i] = li[-i-1]
		li[-i-1] = temp

def reverse2(ListInput):
	RevList=[]
	for i in range(len(ListInput)):
		RevList.append(ListInput.pop())
	return RevList


def reverse3(li):
	for i in range(0, len(li)/2):
		li[i], li[-i - 1] = li[-i - 1], li[i]



l = [1, 2, 3, 4, 5]
reverse(l)
print(l)

l = reverse2(l)
print(l)

reverse3(l)
print l
