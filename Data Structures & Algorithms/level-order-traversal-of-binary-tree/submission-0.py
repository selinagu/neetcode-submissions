# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        left_order = right_order = []
        if root.left:
            left_order = self.levelOrder(root.left)
        if root.right:
            right_order = self.levelOrder(root.right)

        res = [[root.val]]
        if not left_order and not right_order:
            return res
        if len(left_order) >= len(right_order):
            for i in range(len(right_order)):
                res.append(left_order[i] + right_order[i])
            for i in range(len(right_order), len(left_order)):
                res.append(left_order[i])

        else:
            for i in range(len(left_order)):
                res.append(left_order[i] + right_order[i])
            for i in range(len(left_order), len(right_order)):
                res.append(right_order[i])

        return res