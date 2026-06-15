from collections import defaultdict

"""
Problem: 3. Longest Substring Without Repeating Characters
Difficulty: Medium
Topic: Sliding Window
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        char_mp = defaultdict(int)
        max_win_len = 0
        while(j < len(s)):
            char_mp[s[j]] += 1
            while char_mp[s[j]] > 1:
                max_win_len = max(max_win_len, j-i)
                char_mp[s[i]] -= 1
                i += 1
            j += 1
        return max(max_win_len, j-i)
                