
from typing import List

"""
Problem: 217. Contains Duplicate
Difficulty: Easy
Topic: Arrays N Hashing
Link: https://leetcode.com/problems/contains-duplicate/
Date: 2026-06-02
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            
        return False