from typing import List

"""
Problem: 11. Container With Most Water
Difficulty: Medium
Topic: Two Pointers
Link: https://leetcode.com/problems/container-with-most-water/
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA,j,i = 0,len(height)-1,0

        while(i<j):
            if height[i] < height[j]:
                maxA = max(maxA, (height[i]*(j-i)))
                i+=1
            else:
                maxA = max(maxA, (height[j]*(j-i)))
                j-=1
        
        return maxA