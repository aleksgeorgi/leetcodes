# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [(root, 1)]
        max_depth = 0
        
        while stack != []:
            # get the depth and node 
            root, depth = stack.pop()
            max_depth = max(max_depth, depth)
            
            if root.right:
                stack.append((root.right, depth + 1))
            if root.left:
                stack.append((root.left, depth + 1))
                
        return max_depth
            