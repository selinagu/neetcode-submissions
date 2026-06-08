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
                return True

            left_d = depth(root.left)
            right_d = depth(root.right)

            if not left_d or not right_d or abs(left_d - right_d) > 1:
                return False

            return 1 + max(left_d, right_d)

        if not depth(root):
            return False

        return True