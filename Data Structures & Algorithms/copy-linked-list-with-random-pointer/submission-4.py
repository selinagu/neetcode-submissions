"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        if head in self.map:
            return self.map[head]

        copy_head = Node(head.val)
        self.map[head] = copy_head

        copy_head.next = self.copyRandomList(head.next)
        copy_head.random = self.map[head.random] if head.random else None

        return copy_head
