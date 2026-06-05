# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        while heap:
            heap_tail = heapq.heappop(heap)
            tail.next = heap_tail[2]
            i = heap_tail[1]
            tail = tail.next
            if tail.next:
                heapq.heappush(heap, (tail.next.val, i, tail.next))

        return dummy.next
        