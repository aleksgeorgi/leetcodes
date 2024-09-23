class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        # binary search 
        left, right = 2, x//2
        
        while left <= right:
            pivot = left + (right-left) // 2
            num = pivot*pivot
            if x < num:
                right = pivot - 1
            elif x > num:
                left = pivot + 1
            else:
                return pivot 
        return right 