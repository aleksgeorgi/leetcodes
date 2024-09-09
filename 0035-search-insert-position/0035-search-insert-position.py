class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # mark the search boundaries:
        left = 0 
        right = len(nums)-1
        
        # if not found, loop will break when right < left 
        # and the proper position will be found in the value of left 
        while (left <= right):
            pivot = (left + right)//2
        
            if target == nums[pivot]:
                return pivot
            
            elif target < nums[pivot]:
                #look to the left half 
                right = pivot - 1
            
            else: 
                #look to the right half 
                left = pivot + 1
        
        return left
        