"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        node = head

        while node:
            copy_node = Node(x = node.val)
            next_node = node.next
            node.next = copy_node
            copy_node.next = next_node
            node = next_node

        node = head
        while node:
            node.next.random = node.random.next if node.random else None
            node = node.next.next

        node = head
        new_head = head.next
        copy_node = new_head

        while node:
            node.next = copy_node.next
            copy_node.next = node.next.next if node.next else None
            node = node.next
            copy_node = copy_node.next if copy_node else None

        return new_head