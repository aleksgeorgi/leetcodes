class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Idea: 
            - set the first word in the list to be the prefix 
            - iterate through each string in the list
            - for each string, update the prefix by comparing it char by char with the current prefix
                - if a mismatch is found, or either the prefix or the current string ends, 
                  update the prefix to the matched portion
            - return prefix 
        """
        # edge case
        if len(strs) == 1:
            return strs[0]
        # empty list
        if not strs:
            return ""

        prefix = strs[0]
        
        for word in strs[1:]:
            i = 0 
            
            # find the common prefix between the currentw ord and the prefix
            while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
                i+=1
            
            # update the prefix to the common part 
            prefix = prefix[:i]

            # break if prefix is empty
            if not prefix:
                break

        return prefix