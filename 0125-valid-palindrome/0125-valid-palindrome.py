class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        s = s.lower()
        lst = []
        for i in range(len(s)):
            if s[i].isalnum():
                lst.append(s[i])
            
        left, right = 0, len(lst)-1
        
        while left <= right:
            if lst[left] != lst[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True