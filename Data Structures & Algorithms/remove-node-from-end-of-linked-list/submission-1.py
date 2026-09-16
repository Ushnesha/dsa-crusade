# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        p = q = head
        while(i <=n):
            p = p.next
            if not p:
                break
            i += 1
        if not p and i < n:
            return head.next
        while p:
            q = q.next
            p = p.next
        q.next = q.next.next
        return head