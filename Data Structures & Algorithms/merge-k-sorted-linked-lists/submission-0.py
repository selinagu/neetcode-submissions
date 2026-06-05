# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = res = ListNode()

        curs = [node for node in lists if node]

        while curs:
            mini = float("inf")
            mini_idx = -1
            for i in range(len(curs)):
                if curs[i] and curs[i].val < mini:
                    mini = curs[i].val
                    mini_idx = i

            res.next = curs[mini_idx]
            res = res.next     
            curs[mini_idx] = curs[mini_idx].next
            if not curs[mini_idx]:
                curs.pop(mini_idx)

        return dummy.next