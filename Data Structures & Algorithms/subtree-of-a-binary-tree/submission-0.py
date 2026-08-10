# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            if p is None and q is not None:
                return False
            if q is None and p is not None:
                return False
            if p.val == q.val:
                return True and isSameTree(p.right, q.right) and isSameTree(p.left, q.left)
            
            return False
        
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False

        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        