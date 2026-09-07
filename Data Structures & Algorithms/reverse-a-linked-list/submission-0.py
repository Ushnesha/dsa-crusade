# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        p = head
        q = p.next
        if not q: return p
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        head.next = None
        return p