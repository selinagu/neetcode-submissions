# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        linked_list = []
        cur = head
        while cur:
            linked_list.append(cur)
            cur = cur.next

        if len(linked_list) > n:
            prev = linked_list[- n - 1]
            prev.next = prev.next.next
            return head

        return head.next

