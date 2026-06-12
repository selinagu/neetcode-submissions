# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValidSubtree(root):
            if not root:
                return True, float("inf"), float("-inf")

            valid_left, mini_left, maxi_left = isValidSubtree(root.left)
            if not valid_left:
                return False, None, None

            valid_right, mini_right, maxi_right = isValidSubtree(root.right)
            if not valid_right:
                return False, None, None

            if maxi_left < root.val and mini_right > root.val:
                if maxi_left == float("-inf"):
                    mini_left = root.val
                if mini_right == float("inf"):
                    maxi_right = root.val
                    
                return True, mini_left, maxi_right

            return False, None, None

        valid, _, _ = isValidSubtree(root)

        return valid