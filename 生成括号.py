#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-19 17:19:49
# @Author  : wanpeng 
"Generate Parentheses"
#典型的回溯问题
#有多个可行解，每个解由子问题的解构成

def generateparnetthess(n):
	res=[]
	def helper(left,right,n,p):
		if right > left:
			return
		if len(p)==n<<1:
			res.append(p)
		if left < n:
			helper(left+1, right, n, p+'(')
		if right < n:
			helper(left, right+1, n, p+')')
	helper(0, 0, n, '')
	return res

if __name__=="__main__":
	print generateparnetthess(3)
