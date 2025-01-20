class Solution:
    def equalFrequency(self, word: str) -> bool:

        for i in range(len(word)):
            # create a substring with the letter removed 
            subword = word[:i] + word[i+1:]

            # count the frequencies 
            freq = collections.Counter(subword)

            # check if all frequencies are the same 
            if len(set(freq.values())) == 1:
                return True
        
        return False 

