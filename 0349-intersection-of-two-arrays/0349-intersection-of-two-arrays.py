class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1set = set(nums1)
        nums2set = set(nums2)
        
        return list(nums1set.intersection(nums2set))