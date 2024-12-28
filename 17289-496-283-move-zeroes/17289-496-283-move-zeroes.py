class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            l = 0
            for r in range(len(nums)):
                if nums[r]!=0 and nums[l]==0:
                    nums[l], nums[r] = nums[r], nums[l]
                if nums[l]!=0:
                    l +=1
            

                        
