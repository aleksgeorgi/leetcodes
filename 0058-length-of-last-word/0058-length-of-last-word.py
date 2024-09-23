class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0 
        for char in range(len(s)-1, -1, -1):
            if s[char] == ' ' and counter > 0:
                return counter
            elif s[char] == ' ':
                continue 
            else: 
                counter += 1
                
        return counter
                
                
                
                
                
        
        