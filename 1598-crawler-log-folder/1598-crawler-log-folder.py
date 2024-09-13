class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        '''
        pseudo:
        stack = []
        
        for each element in logs
            if not elem.isalnum():
                if stack != 0 and elem == "../"
                    pop
                if elem = "./"
                    continue 
            else
                push elem

        return len(stack)
        
        '''
        
        stack = []
        
        for elem in logs:
            elem = elem.replace("/", "")
            if not elem.isalnum():
                if len(stack) != 0 and elem == "..":
                    stack.pop()
                else:
                    continue
            else:
                stack.append(elem)
                
        return len(stack)