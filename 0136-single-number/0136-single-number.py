class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        map_count = collections.Counter(nums)
        
        for key, value in map_count.items():
            if value == 1:
                return int(key)
            
        return -1
        