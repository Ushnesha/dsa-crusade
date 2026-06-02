from typing import List

"""
Problem: 1. Two Sum
Difficulty: Easy
Topic: Arrays N Hashing
Link: https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ctr = {}
        for i,num in enumerate(nums):
            if num in ctr:
                return [ctr[num], i]
            ctr[target-num] = i
        
        