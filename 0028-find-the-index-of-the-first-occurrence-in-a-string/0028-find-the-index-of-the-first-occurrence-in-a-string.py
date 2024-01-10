class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        idea without built in functions (substring)
        want to use two pointers to solve 
        
        '''

        if not needle:
            return 0  # edge case if needle is empty

        hay_start = 0
        i = 0
        j = 0

        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):  # check for complete match
                    return hay_start
            else:
                j = 0
                hay_start += 1
                i = hay_start

        return -1
                
            