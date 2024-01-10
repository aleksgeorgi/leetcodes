class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        idea
        
        iterate through the list right to left
        use a set to store numbers you've seen so far
        if a number is already in the set, pop it in place
        '''
        
        seen = set()
        i = 0
        while i < len(nums):
            if nums[i] in seen:
                nums.pop(i)
            else:
                seen.add(nums[i])
                i += 1
                
        return len(seen)