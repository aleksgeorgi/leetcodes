class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1p = 0 
        w2p = 0
        res = []

        while w1p < len(word1) and w2p < len(word2):
            res += (word1[w1p])
            w1p += 1
            res += (word2[w2p])
            w2p += 1
        
        if w1p < len(word1):
            res += (word1[w1p::])
        if w2p < len(word2):
            res += (word2[w2p::])

        return "".join(res)