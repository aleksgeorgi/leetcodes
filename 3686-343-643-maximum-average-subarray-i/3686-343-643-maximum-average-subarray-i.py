class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[:k]) # sum the first k elements
        maxSum = currSum

        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i-k] # update the sum with sliding window
            maxSum = max(maxSum, currSum)

        return maxSum/k