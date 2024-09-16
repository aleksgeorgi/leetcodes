class Solution:
    def climbStairs(self, n: int) -> int:
        # decalre a memo to store recursive computations 
        memo = [0] * (n+1)
        return self.climb_stairs(0, n, memo)
        
    def climb_stairs(self, i: int, n: int, memo: List[int]) -> int:
        if i > n:
            return 0 # you've gone too far 
        if i == n:
            return 1 # only one way to get to where you are 
            
        if memo[i] > 0:
            return memo[i]
            
        memo[i] = self.climb_stairs(i+1, n, memo) + self.climb_stairs(i+2, n, memo)
        
        return memo[i]