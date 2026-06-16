# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")

        def maxPath(node):
            nonlocal max_path

            if not node:
                return 0

            left = maxPath(node.left)
            right = maxPath(node.right)
            max_path_node = max(0, left) + max(0, right) + node.val
            max_path = max(max_path, max_path_node)

            return max(max(0, left), max(0, right)) + node.val

        maxPath(root)

        return max_path