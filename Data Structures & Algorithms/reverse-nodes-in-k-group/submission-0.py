# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = last_head = ListNode()
        while True:
            num = 0
            cur = head
            while cur:
                num += 1
                if num == k:
                    break
                cur = cur.next

            if num == k:
                next_head = cur.next

                node = head
                prev = None
                for i in range(k):
                    next_node = node.next
                    node.next = prev
                    prev = node
                    node = next_node

                last_head.next = cur
                last_head = head
                head = next_head

            else:
                last_head.next = head
                break
                
        return dummy.next