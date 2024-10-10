class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        
        for index in range(len(nums)):
            if nums[index] not in numsMap:
                numsMap[nums[index]] = index
        print(numsMap)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numsMap and numsMap[diff] != i:
                return[i, numsMap[diff]]
            
        return [-1,-1]
                
                
        