class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break # bc array is sorted it's impossible to find subsequent numbers to add to 0
            if i == 0 or nums[i - 1] != nums[i]: # if it's the first element or not a duplicate
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo = i+1
        hi = len(nums) - 1
        
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1 # we only need to prevent duplicates in low since we're
                    # already preventing duplicates in i so that will guarantee no duplicate
                    # triples will be added