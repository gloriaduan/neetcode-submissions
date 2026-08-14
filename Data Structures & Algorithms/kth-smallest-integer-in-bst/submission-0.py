# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = []

        def preorder(root, q):
            if root is None:
                return
            
            preorder(root.left, q)
            q.append(root.val)
            preorder(root.right, q)
        
        preorder(root, q)

        return q[k-1]