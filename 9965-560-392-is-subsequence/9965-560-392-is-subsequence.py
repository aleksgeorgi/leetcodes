class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True

        sp = 0 # s pointer

        for tp in range(len(t)):
            if sp < len(s) and t[tp] == s[sp]:
                sp += 1 # look for the next match in s 
            
        return sp == len(s) 
        