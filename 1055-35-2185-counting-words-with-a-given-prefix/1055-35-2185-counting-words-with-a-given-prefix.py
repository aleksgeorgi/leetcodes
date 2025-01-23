class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # sort words by length 
        words.sort()
        pref_len = len(pref)
        count = 0

        for word in words:
            if len(word) < pref_len:
                continue
            else:
                if word[:pref_len] == pref:
                    count += 1

        return count