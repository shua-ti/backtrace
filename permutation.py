#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-19 17:33:45
# @Author  : wanpeng
"置换"

def permutations(nums):
    res =[]
    size=len(nums)
    def dfs(nums,pattern):
        if len(pattern)==size:
            res.append(pattern)
            return
        i=0
        while i <len(nums):
            dfs(nums[:i]+nums[i+1:],pattern+[nums[i]])
            while i <len(nums)-1 and nums[i]==nums[i+1]:
            	i+=1  
            i+=1
    dfs(nums,[])
    return res

if __name__=="__main__":
	print permutations([1,1,2])
