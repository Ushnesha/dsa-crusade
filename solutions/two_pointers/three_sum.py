from typing import List

"""
Problem: 15. 3Sum
Difficulty: Medium
Topic: Two Pointers
Link: https://leetcode.com/problems/3sum/
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while(nums[j] == nums[j-1] and j < k):
                        j += 1
                
        return res