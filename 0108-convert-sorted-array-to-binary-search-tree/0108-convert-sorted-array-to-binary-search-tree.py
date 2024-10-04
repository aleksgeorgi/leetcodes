# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: if the array is empty, return None
        if not nums:
            return None
        
        # Call the helper function to build the BST
        return self.buildBST(nums, 0, len(nums) - 1)
    
    def buildBST(self, array, low, high):
        # Base case: if no elements left to process, return None
        if low > high:
            return None
        
        # Find the middle index
        mid = (low + high) // 2
        
        # Create the root node with the middle value
        root = TreeNode(array[mid])
        
        # Recursively build the left subtree
        root.left = self.buildBST(array, low, mid - 1)
        
        # Recursively build the right subtree
        root.right = self.buildBST(array, mid + 1, high)
        
        return root