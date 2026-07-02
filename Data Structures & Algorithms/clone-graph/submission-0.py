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

        new_node = Node(val = node.val)
        old_to_new = {node: new_node}

        def dfs(cur, new_cur):

            if cur.neighbors is None:
                return

            for nbr in cur.neighbors:
                if nbr in old_to_new:
                    new_nbr = old_to_new[nbr]
                else:
                    new_nbr = Node(val = nbr.val)
                    old_to_new[nbr] = new_nbr
                    dfs(nbr, new_nbr)
                    
                new_cur.neighbors.append(new_nbr)

        dfs(node, new_node)

        return new_node