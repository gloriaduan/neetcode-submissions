"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}

        def clone(node):
            if node is None:
                return None 
                
            cur = Node(node.val)
            cloned[node] = cur
            for n in node.neighbors:
                if n not in cloned:
                    cur.neighbors.append(clone(n))
                else:
                    cur.neighbors.append(cloned[n])
            
            return cur
        
        return clone(node)
                
            

