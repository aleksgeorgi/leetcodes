# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # preorder traversal 
        listp = []
        self.preorder(p, listp)
        
        listq = []
        self.preorder(q, listq)
        
        if len(listp) != len(listq):
            return False
        
        for i in range(len(listp)-1):
            if listp[i] != listq[i]:
                return False 
        
        return True
        
    def preorder(self, root, lst):
        if root is not None:
            lst.append(root.val)
            self.preorder(root.left, lst)
            self.preorder(root.right, lst)
        else:
            lst.append(None)
                