class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.bin_search(nums, 0, len(nums) - 1)

    def bin_search(self, nums, l, r):
        if l==r:
            return l
        mid = (l+r)//2

        # descending slope 
        if nums[mid] > nums[mid +1]:
            return self.bin_search(nums, l, mid)
        # ascending slope
        return self.bin_search(nums, mid+1, r)

    # time: O(logn) bc of binary search 
    # space: O(logn) bc of recursive depth 

