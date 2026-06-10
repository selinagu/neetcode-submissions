# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        def findpq(root, node):
            if not root:
                return False
            if findpq(root.left, node) or findpq(root.right, node) or root.val == node.val:
                return True
            return False

        queue = [root]
        nodes = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                nodes.append(node.left)
            if node.right:
                queue.append(node.right)
                nodes.append(node.right)

        for i in range(len(nodes) - 1, -1, -1):
            node = nodes[i]
            if findpq(node, p) and findpq(node, q):
                return node

