class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2): 
            for j in range(n // 2): 
                temp = matrix[n-j-1][i] # bottom left 
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]# bottom right
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1] # top right
                matrix[j][n-i-1] = matrix[i][j] # top left
                matrix[i][j] = temp
                
        
                
                
                
                
                
                
                
                
                
                
                
        #         tmp = matrix[n - 1 - j][i]
        #         matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
        #         matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
        #         matrix[j][n - 1 - i] = matrix[i][j]
        #         matrix[i][j] = tmp
