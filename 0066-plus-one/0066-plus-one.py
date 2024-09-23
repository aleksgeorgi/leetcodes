class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in range(len(digits)):
            s += str(digits[i])        
        
        result = 1+int(s)
        result = str(result)
        
        result_list=[]
        
        for i in range(len(result)):
            result_list.append(int(result[i]))    
        
        return result_list