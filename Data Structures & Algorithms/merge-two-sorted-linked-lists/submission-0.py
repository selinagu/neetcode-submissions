# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        prev = ListNode()
        cur = None
        dummy = prev

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur = cur1
                cur1 = cur1.next
            else:
                cur = cur2
                cur2 = cur2.next
            prev.next = cur
            prev = cur
        if cur1:
            cur = cur1
            cur1 = cur1.next
            prev.next = cur
            prev = cur
        if cur2:
            cur = cur2
            cur2 = cur2.next
            prev.next = cur
            prev = cur

        return dummy.next