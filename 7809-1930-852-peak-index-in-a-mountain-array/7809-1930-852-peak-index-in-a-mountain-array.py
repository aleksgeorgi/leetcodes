class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1

        while l < r:
            mid = (l+r)//2
            # increasing slope, move right 
            if arr[mid] < arr[mid+1]:
                l = mid + 1
            # decreasing slope, move left 
            else:
                r = mid 
        return l 

    # time: O(logn) for bin search
    # space: O(1) for vars l, r, mid 


