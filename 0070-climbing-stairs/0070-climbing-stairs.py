class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        
        '''
        recurrence relation F(n) = F(n-1) + F(n-2)
        
        base cases:
        F(0) = 1
        F(1) = 1
        '''
        
        prev1, prev2 = 1, 1 # base cases
        
        #calculate F(n) iteratively 
        for i in range(2, n+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current 
        
        return prev1
        