class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # table for calculating max seen so far 
        max_dp = [0]*len(nums)

        max_dp[0] = nums[0] # initialize the first subarray sum as max
        
        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i-1] + nums[i], nums[i])

        return max(max_dp)
        
        # time: O(n) bc single pass to init max_dp + single pass for loop = 2n ~ n
        # space: O(n) bc max_dp = n 