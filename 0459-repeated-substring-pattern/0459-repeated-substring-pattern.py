class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        if len(s) == 2:
            if s[0] != s[1]:
                return False
        
        substring = []
        i = 0 
        
        while i <= len(s)//2:
            substring.append(s[i])
            if ("".join(substring))*(len(s)//len(substring)) == s:
                print("".join(substring)*(len(s)//len(substring)))
                return True
            else: 
                i+=1
                
        return False 