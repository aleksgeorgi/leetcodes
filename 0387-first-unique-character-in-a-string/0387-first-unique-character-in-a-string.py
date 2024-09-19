class Solution:
    def firstUniqChar(self, s: str) -> int:
        # hashmap way 
        seen = {}
        
        #iterate through once to add the letter counts to the hashmap
        for char in s:
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] = seen.get(char) + 1
                
        # if all vals > 1 return -1 
        if all( value > 1 for value in seen.values()):
            return -1 
        
        # iterate through string and return the first char that has val of 1
        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i