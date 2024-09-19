class Solution:
    def firstUniqChar(self, s: str) -> int:
        # brute force way 
        seen = set()
        
        # Outer loop: Iterate over each character
        for i in range(len(s)):
            if s[i] in seen:
                continue
            
            is_unique = True
            
            # Inner loop: Compare the current character with every other character
            for j in range(len(s)):
                if i != j and s[i] == s[j]:
                    is_unique = False
                    seen.add(s[i])
                    break
                    
            # If no other character matched, it's the first non-repeating character
            if is_unique:
                return i

        # If no unique character is found, return -1
        return -1