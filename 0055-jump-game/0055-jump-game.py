class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False  # If we can't reach this index, return False
            farthest = max(farthest, i + nums[i])  # Update the farthest position we can reach
            if farthest >= len(nums) - 1:  # If we can reach or exceed the last index
                return True
        return True
    
