import math
from collections import defaultdict

"""
Problem: 76. Minimum Window Substring
Difficulty: Hard
Topic: Sliding Window
Link: https://leetcode.com/problems/minimum-window-substring/
"""

class Solution:
    
    def has_space(self, d):
        for k,v in d.items():
            if v > 0:
                return True
        return False
    def minWindow(self, s: str, t: str) -> str:
        mem = []
        min_win = math.inf
        t_dict = defaultdict(int)
        final_st_idx, final_ed_idx = -1, -1
        res = ""
        for t_n in t:
            t_dict[t_n] += 1
        i, j = 0, 0
        while j < len(s):
            if s[j] in t_dict:
                t_dict[s[j]] -= 1
            # else:
            #     continue
                
                while not self.has_space(t_dict):
                    if min_win > j - i + 1:
                        min_win = j - i + 1
                        final_st_idx, final_ed_idx = i, j
                    if s[i] in t_dict:
                        t_dict[s[i]] += 1
                    i += 1
                
            j += 1
        return s[final_st_idx: final_ed_idx+1]