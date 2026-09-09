# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _revlist(self,  head: Optional[ListNode]) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        p = head
        n = 0
        while p:
            n+=1
            p = p.next
            
        p = head
        for i in range(n//2):
            p = p.next
        q = self._revlist(p.next)
        p.next = None
        p = head
        while p and q:
            pn = p.next
            p.next = q
            p = pn
            qn = q.next
            q.next = p
            q = qn