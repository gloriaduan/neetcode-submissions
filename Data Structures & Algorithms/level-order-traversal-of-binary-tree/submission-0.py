# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack = []

        if root:
            stack.append((root, 0))

        while stack:
            el = stack.pop(0)
            el_depth = el[1]
            el_node = el[0]
            el_value = el_node.val

            if el_depth > len(res) - 1:
                res.append([el_value])
            else:
                res[el_depth].append(el_value)
            
            if el_node.left:
                stack.append((el_node.left, el_depth + 1))
            if el_node.right:
                stack.append((el_node.right, el_depth + 1))
        
        return res