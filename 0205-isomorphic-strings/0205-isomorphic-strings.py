class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        
        for i, j in zip(s,t):
            if i not in smap:
                if j in tmap:
                    return False
                else:
                    smap[i] = j
                    tmap[j] = i
            else:
                if smap[i] != j:
                    return False
            
        return True
            
        