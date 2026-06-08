# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(root):
            if not root:
                return 0

            left_d = depth(root.left)
            if left_d == -1:
                return -1

            right_d = depth(root.right)
            if right_d == -1:
                return -1

            if abs(left_d - right_d) > 1:
                return -1

            return 1 + max(left_d, right_d)

        if depth(root) == -1:
            return False

        return True