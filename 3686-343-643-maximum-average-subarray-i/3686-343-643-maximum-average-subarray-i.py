class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        sumArr = [0]*n # for a running sum helper
        sumArr[0] = nums[0] # initialize the first sum as is 

        # populate running sum
        for i in range(1,n):
            sumArr[i] = nums[i]+sumArr[i-1]

        maxAvg = sumArr[k-1]/k # get the first possible max avg at index k-1

        # find the max avg
        for i in range(k,n):
            currAvg = (sumArr[i] - sumArr[i-k])/k
            maxAvg = max(maxAvg, currAvg)
        
        return maxAvg
