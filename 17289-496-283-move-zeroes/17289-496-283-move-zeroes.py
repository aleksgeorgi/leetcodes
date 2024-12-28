class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def _swap(arr, l, r):
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp

        if len(nums) > 1:
            l = 0
            r = l+1

            while r < len(nums):
                if nums[l]==0:
                    while r < len(nums) and nums[r]==0:
                        r += 1
                    if r < len(nums):
                        _swap(nums, l, r)
                l += 1
                r = l+1
            

                        
