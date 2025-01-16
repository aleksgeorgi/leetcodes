class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        leftp = [0]*n   # left product
        rightp = [0]*n  # right product
        answer = [0]*n  # solution list

        leftp[0] = 1 
        rightp[-1] = 1

        # populate the left product array 
        for i in range(1, n):
            leftp[i] = nums[i-1] * leftp[i-1]

        # populate the right product array 
        for i in range(n-2, -1, -1):
            rightp[i] = rightp[i+1] * nums[i+1]

        for i in range(n):
            answer[i] = leftp[i]*rightp[i]

        return answer