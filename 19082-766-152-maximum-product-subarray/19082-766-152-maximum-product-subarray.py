class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max(curr*max_so_far, curr*min_so_far))
            min_so_far = min(curr, min(curr*max_so_far, curr*min_so_far))

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result
    
    # time: O(n) bc of one for-loop
    # space: O(1) bc of vars 