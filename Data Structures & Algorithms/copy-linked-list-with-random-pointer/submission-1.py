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
        full_list = []
        while head:
            full_list.append(head)
            head = head.next

        rand_idx = [None] * len(full_list)
        for i in range(len(full_list)):
            cur = full_list[i]
            rand = cur.random
            for j in range(len(full_list)):
                if full_list[j] == rand:
                    rand_idx[i] = j

        copy_list = [Node(0) for _ in range(len(full_list))]
        for i in range(len(full_list)):
            copy_list[i].val = full_list[i].val
            copy_list[i].next = copy_list[i + 1] if i < len(full_list) - 1 else None
            if rand_idx[i] is not None:
                copy_list[i].random = copy_list[rand_idx[i]]

        if copy_list: 
            return copy_list[0]
        return None