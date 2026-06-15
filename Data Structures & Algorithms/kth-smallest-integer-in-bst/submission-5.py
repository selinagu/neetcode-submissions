# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        num = 0

        def dfs(root):
            nonlocal num
            if not root:
                return 

            dfs(root.left)
            arr.append(root.val)
            num += 1
            if num == k:
                return root
            dfs(root.right)

        dfs(root)
        return arr[k-1]