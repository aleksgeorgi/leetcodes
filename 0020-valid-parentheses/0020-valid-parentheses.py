class Solution:
    def isValid(self, s: str) -> bool:
        
        # list for stack
        stack = []
        # dictionary to hold mapping 
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            # is char is one of the keys in mapping?
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack