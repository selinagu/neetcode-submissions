# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p and queue_q:
            node1 = queue_p.popleft()
            node2 = queue_q.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            queue_p.append(node1.left)
            queue_p.append(node1.right)
            queue_q.append(node2.left)
            queue_q.append(node2.right)

        return True