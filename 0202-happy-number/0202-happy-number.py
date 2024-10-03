class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        # edge cases
        if n==1:
            return True
        
        # parsing loop
        while n != 1:
            n = self.getNSum(n)
            # print("n: ", n)
            if n == 1:
                return True
            if n in seen:
                break
            else:
                seen.add(n)
                
        return False
        
        
    def getNSum(self, n: int) -> int:
        nSum = 0
        # parsing loop:
        while n > 0: 
            # get the last digit
            endDigit = n%10
            # remove the last number
            n = n//10
            
            nSum += (endDigit**2)
        
        return nSum
            