"""
Problem: 125. Valid Palindrome
Difficulty: Easy
Topic: Two Pointers
Link: https://leetcode.com/problems/valid-palindrome/
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = ""
        for ch in s:
            if ch.isalnum():
                s_ = s_ + ch.lower()
        i , j = 0 , len(s_) - 1
        while i < len(s_)/2:
            if s_[i] != s_[j]:
                return False
            i = i + 1
            j = j - 1
        return True

        