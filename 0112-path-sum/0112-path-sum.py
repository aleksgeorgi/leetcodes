# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        use BFS with a queue to traverse the tree
        if root.left is null or root.right is null meaning we've reaching a leaf, 
            compare the sum against the target 
        if the sum does not equal the target, subtract the value of the node and backtrack
        if the sum does equal the target, return true
        keep going until all nodes have been explored. 
        if all nodes have been explored, return false 
        '''
        
        if not root:
            return False
        
        #queue for BFS, holding the tuple of (node, current_path_sum)
        queue = collections.deque([(root, root.val)])
        
        while queue: 
            # get the working node 
            node, current_path_sum = queue.popleft()
            
            # check if it's a leaf node
            if not node.left and not node.right:
                if current_path_sum == targetSum:
                    return True
            
            # process the left child 
            # add the left child to the queue and add the current value to the sum
            if node.left:
                queue.append((node.left, current_path_sum + node.left.val))
            
            # process the right child 
            if node.right:
                queue.append((node.right, current_path_sum + node.right.val))
                
            
        return False # no path sum equals target 
            
            
        