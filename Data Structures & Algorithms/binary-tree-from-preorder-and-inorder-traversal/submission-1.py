# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        inorder_idx = {val: i for i, val in enumerate(inorder)}
        pre_idx = -1
        
        def build(left, right):
            nonlocal pre_idx
            
            if left > right:
                return None

            pre_idx += 1
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            in_idx = inorder_idx[root_val]

            root.left = build(left, in_idx - 1)
            root.right = build(in_idx + 1, right)

            return root

        return build(0, len(inorder) - 1)