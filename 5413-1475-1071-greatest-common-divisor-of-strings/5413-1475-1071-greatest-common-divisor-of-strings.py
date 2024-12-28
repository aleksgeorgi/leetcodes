class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        substring = ""
        index = 0
        res = []

        while(index < len(str1)):
            substring += str1[index] 
            if substring*round(len(str1)/len(substring)) == str1 and substring*round(len(str2)/len(substring)) == str2:
                res.append(substring)
            index += 1

        
        return res[-1] if len(res) > 0 else ""
        