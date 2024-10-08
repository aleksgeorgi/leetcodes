class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # check if same
        if mat == target:
            return True
        
        # at most 4 rotations before returning to start 
        n = len(mat[0])
        for _ in range(3):
            for i in range(n//2 + n%2):
                for j in range(n//2):
                    temp = mat[n-j-1][i]
                    mat[n-j-1][i] = mat[n-i-1][n-j-1]
                    mat[n-i-1][n-j-1] = mat[j][n-i-1]
                    mat[j][n-i-1] = mat[i][j]
                    mat[i][j] = temp
                    
            if mat == target:
                return True
            
        return False 