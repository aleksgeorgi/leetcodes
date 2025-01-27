class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res = []
        for i in range(1, len(mountain) - 1):
            if mountain[i - 1] < mountain[i] > mountain[i + 1]:
                res.append(i)
        return res
    
    # time O(n) for single loop
    # space O(n) for the array of peaks 