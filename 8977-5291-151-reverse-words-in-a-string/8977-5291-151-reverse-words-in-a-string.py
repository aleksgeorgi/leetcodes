class Solution:
    def reverseWords(self, s: str) -> str:

        sSplit= s.split() # split into list of words 
        revList = []

        for word in sSplit:
            revList.insert(0, word)

        revString = " ".join(revList)

        return revString
