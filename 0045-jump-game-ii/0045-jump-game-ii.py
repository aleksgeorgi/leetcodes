class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize variables
        jumps = 0       # Number of jumps made
        farthest = 0    # The farthest we can reach
        current_end = 0 # The end of the current jump range
        
        # We don't need to process the last element (nums[n-1]), hence len(nums)-1
        for i in range(len(nums) - 1):
            # Update the farthest point we can reach from the current index
            farthest = max(farthest, i + nums[i])
            
            # If we have reached the end of the current jump range, make a jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If the farthest point we can reach is already at or beyond the last index, we're done
                if current_end >= len(nums) - 1:
                    break
        
        return jumps
