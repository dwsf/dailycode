#!/usr/bin/python
#coding:utf-8
#author:zsc347
#create on 2013-8-29
A=[2,2,1,0,1]

def solution(A):
	hasht={}
	a=[]
	for ls in A:
		if hasht.has_key(ls):
			a.append(True)
		else:
			a.append(False)
			hasht[ls]=True
	print hasht
	print a
	length=len(a)-1
	while length>0:
		if a[length]:
			length-=1
		else:
			break
	return length
		

print solution(A)
