# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.n = n

        def rec(cur):
            if not cur:
                return None

            cur.next = rec(cur.next)
            self.n -= 1
            if self.n == 0:
                return cur.next
            return cur

        return rec(head)
