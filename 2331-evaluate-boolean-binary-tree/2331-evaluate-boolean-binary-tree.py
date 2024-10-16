# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # if its a leaf: return the T/F value 
        # if it's not a leaf: evaluate it's children based on it's boolean op
        return self._postOrder_traversal(root)
        
    def _postOrder_traversal(self, root):
        if not root:
            return None
        # if it's a leaf
        elif not root.left and not root.right:
            return root.val
        
        # not a leaf
        elif root.val == 2: # OR
            return (
                self._postOrder_traversal(root.left) or
                self._postOrder_traversal(root.right)
            )
        else:
            return(
                self._postOrder_traversal(root.left) and
                self._postOrder_traversal(root.right)
            )
        
        