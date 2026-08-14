# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = []

        def inorder(root, q):
            if root is None:
                return
            
            inorder(root.left, q)
            q.append(root.val)
            inorder(root.right, q)
        
        inorder(root, q)

        return q[k-1]