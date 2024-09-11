class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix) # number of rows because each element is a row
        n = len(matrix[0]) # number of columns 
        
        # binary search to find the correct row 
        top_p = 0 
        bottom_p = m - 1
        target_row = 0
        
        while (top_p <= bottom_p):
            middle_p = (bottom_p+top_p)//2
            if target == matrix[middle_p][0]:
                 return True
            elif target < matrix[middle_p][0]:
                bottom_p = middle_p - 1
            else:
                top_p = middle_p + 1 
                
        # After the loop, check where the bottom pointer 
        # points to decide the target row
        if bottom_p < 0:
            return False  # All values in matrix are greater than target

        target_row = bottom_p  # Use the last valid row index where target could be
           
        # binary search to find the correct index in the row
        left_p = 0
        right_p = n-1
        
        while left_p<=right_p:
            middle_p = (left_p + right_p)//2
            
            if target == matrix[target_row][middle_p]:
                return True
            elif target < matrix[target_row][middle_p]:
                right_p = middle_p-1
            else:
                left_p = middle_p+1
        
        return False
        