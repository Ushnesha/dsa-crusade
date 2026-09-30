from typing import Optional

"""
Problem: 138. Copy List with Random Pointer
Difficulty: Medium
Topic: Linked List
Link: https://leetcode.com/problems/copy-list-with-random-pointer/
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = None
        node_map = {}
        p = head
        while p:
            new_node = Node(p.val)
            if not new_head:
                new_head = new_node
            node_map[p] = new_node
            p = p.next
        for (ll, copyll) in node_map.items():
            copyll.next = node_map[ll.next] if ll.next else None
            copyll.random = node_map[ll.random] if ll.random else None
        return new_head
        