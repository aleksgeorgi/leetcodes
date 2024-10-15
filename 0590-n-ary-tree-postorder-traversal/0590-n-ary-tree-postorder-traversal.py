"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
                
        if not root:
            return root
        
        self._traverse_postorder(root, result)
            
        return result
        
    def _traverse_postorder(self, node, result):
        if not node:
            return 
        
        for child in node.children:
            self._traverse_postorder(child, result)
            
        result.append(node.val)
                
        