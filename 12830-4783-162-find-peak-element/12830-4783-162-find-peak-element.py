class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l+r)//2
            # descending slope, move left
            if nums[mid] > nums[mid+1]:
                r = mid
            # ascending slope, move right
            else:
                l = mid + 1

        return l

        # time: O(logn) due to binary search
        # space: O(1) due to variables 

