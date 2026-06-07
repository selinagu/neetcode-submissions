# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def divide(lists, l, r):
            if l > r:
                return None
            if l == r:
                return lists[l]

            mid = (l + r) // 2
            left = divide(lists, l, mid)
            right = divide(lists, mid+1, r)

            dummy = cur = ListNode()
            while left and right:
                if left.val <= right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next

            if left:
                cur.next = left
            if right:
                cur.next = right

            return dummy.next

        return divide(lists, 0, len(lists) - 1)