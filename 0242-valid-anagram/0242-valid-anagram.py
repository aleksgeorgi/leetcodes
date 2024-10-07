class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = collections.Counter(s)
        tMap = collections.Counter(t)
        
        return sMap == tMap