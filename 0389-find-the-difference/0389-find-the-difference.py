class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) < 1:
            return t
        
        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)
        
        for letter, count in t_dict.items():
            if s_dict[letter] != count:
                return letter
        return ""