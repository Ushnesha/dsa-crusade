from typing import Optional

"""
Problem: 2. Add Two Numbers
Difficulty: Medium
Topic: Linked List
Link: https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l3 = p = None
        while l1 or l2:
            sm = carry
            if l1:
                sm += l1.val
                l1 = l1.next
            if l2:
                sm += l2.val
                l2 = l2.next
            new_node = ListNode(sm%10)
            carry = sm//10
            if not l3:
                l3 = new_node
                p = l3
            else:
                p.next = new_node
                p = p.next
        while carry:
            new_node = ListNode(carry%10)
            p.next = new_node
            p = p.next
            carry = carry//10
        return l3
            