# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        num = 0
        stack = [(root, root.val)]
        while stack:
            node, max_val = stack.pop()
            if max_val <= node.val:
                num += 1
            if node.left:
                stack.append((node.left, max(max_val, node.left.val)))
            if node.right:
                stack.append((node.right, max(max_val, node.right.val)))

        return num