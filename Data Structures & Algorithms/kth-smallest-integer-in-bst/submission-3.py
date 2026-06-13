# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        stack = [root]
        node = root
        while stack:
            while node.left:
                node = node.left
                stack.append(node)
            
            k -= 1
            if k == 0:
                return node.val
            stack.pop()

            while not node.right:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val

            node = node.right
            stack.append(node)

        return None