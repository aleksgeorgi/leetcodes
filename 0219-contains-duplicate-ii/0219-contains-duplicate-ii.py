class Solution:
    def containsNearbyDuplicate(self, nums, k):
        num_set = set()

        for i in range(len(nums)):
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])

            # Keep the window size to k
            if len(num_set) > k:
                num_set.remove(nums[i - k])

        return False
