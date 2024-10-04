from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        countMag = Counter(magazine)
        countRand = Counter(ransomNote)
        
        for key, value in countRand.items():
            if key not in countMag or countRand.get(key) > countMag.get(key):
                return False
            
        return True
                
            