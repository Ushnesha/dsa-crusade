from typing import List

"""
Problem: 153. Find Minimum in Rotated Sorted Array
Difficulty: Medium
Topic: Binary Search
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        l,r=0,n-1
        while l <= r:
            m = (l+r)//2
            if nums[l] <= nums[m] and nums[m+1] <= nums[r]:
                return min(nums[l],nums[m+1])
            elif nums[l] > nums[m]:
                r = m
            else:
                l = m+1
                