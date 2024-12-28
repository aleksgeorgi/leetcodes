class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            l = 0
            r = l+1

            while r < len(nums):
                if nums[l]==0:
                    while r < len(nums) and nums[r]==0:
                        r += 1
                    if r < len(nums):
                        nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r = l+1
            

                        
