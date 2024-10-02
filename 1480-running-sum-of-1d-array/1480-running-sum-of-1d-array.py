class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        runSumArr = [0]*len(nums)
        runSumArr[0] = nums[0]
     
        for i in range(1, len(nums)):
            runSumArr[i] = nums[i]+runSumArr[i-1]
            
        return runSumArr