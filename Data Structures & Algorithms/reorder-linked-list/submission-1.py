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
        p = q = head
        while p and p.next and p.next.next:
            p = p.next.next
            q = q.next
        rev_q = self._revlist(q.next)
        q.next = None
        q = rev_q
        p = head
        while p and q:
            pn = p.next
            p.next = q
            p = pn
            qn = q.next
            q.next = p
            q = qn