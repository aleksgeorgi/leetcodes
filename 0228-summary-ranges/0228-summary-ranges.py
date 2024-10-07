class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        i = 0 
        
        while i < len(nums):
            start = nums[i]
            
            while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                i += 1 
                
            if start != nums[i]:
                output.append(str(start) + "->" + str(nums[i]))
            else:
                output.append(str(start))
                
            i += 1
            
        return output
            