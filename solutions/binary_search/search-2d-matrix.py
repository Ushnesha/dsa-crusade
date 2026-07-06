from typing import List

"""
Problem: 74. Search a 2D Matrix
Difficulty: Medium
Topic: Binary Search
Link: https://leetcode.com/problems/search-a-2d-matrix/
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while(l<=r):
            mid = (l+r)//2
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] < target:
                l = mid+1
            else:
                r = mid-1
        return False
    
    