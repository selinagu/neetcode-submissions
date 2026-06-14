# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [root]
        node = root
        depths = {}

        while stack:
            node = stack[-1]
            if (not node.left or node.left in depths) and (not node.right or node.right in depths):
                stack.pop()
                left_h = depths.get(node.left, 0)
                right_h = depths.get(node.right, 0)
                if abs(left_h - right_h) > 1:
                    return False

                depths[node] = 1 + max(left_h, right_h)

            if node.left and node.left not in depths:
                stack.append(node.left)
                node = node.left
            
            if node.right and node.right not in depths:
                stack.append(node.right)
                node = node.right

        return True