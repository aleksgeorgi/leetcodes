class Solution:
    def reverseVowels(self, s: str) -> str:

        s_array = list(s)

        left = 0
        right = len(s)-1
        vowel = "aeiouAEIOU"
        left_vowel = None
        right_vowel = None 

        while left < right:
            if s_array[left] not in vowel:
                left+=1
            else:
                left_vowel = s_array[left]

            if s_array[right] not in vowel:
                right-=1 
            else:
                right_vowel = s_array[right]
            
            if left_vowel and right_vowel:
                s_array[left], s_array[right] = s_array[right], s_array[left]
                left+=1
                right-=1
                left_vowel = None
                right_vowel = None 

        return "".join(s_array)