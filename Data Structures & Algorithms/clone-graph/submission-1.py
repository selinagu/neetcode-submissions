"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        old_to_new = {}
        
        def dfs(cur):
            if cur in old_to_new:
                return old_to_new[cur]

            new_cur = Node(val = cur.val)
            old_to_new[cur] = new_cur

            for nbr in cur.neighbors:
                new_cur.neighbors.append(dfs(nbr))

            return new_cur

        return dfs(node)