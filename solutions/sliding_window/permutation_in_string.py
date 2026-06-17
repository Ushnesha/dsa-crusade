"""
Problem: 567. Permutation in String
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/permutation-in-string/
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        gbl_lst = [0]*26
        loc_lst = [0]*26
        for i in range(len(s1)):
            gbl_lst[ord(s1[i]) - ord('a')] += 1
            loc_lst[ord(s2[i]) - ord('a')] += 1
        i,j = 0,len(s1)-1
        while j < len(s2):
            if gbl_lst == loc_lst:
                return True
            if j == len(s2) - 1:
                return False
            else:
                loc_lst[ord(s2[i]) - ord('a')] -= 1
                i += 1
                j += 1
                loc_lst[ord(s2[j]) - ord('a')] += 1
        return False