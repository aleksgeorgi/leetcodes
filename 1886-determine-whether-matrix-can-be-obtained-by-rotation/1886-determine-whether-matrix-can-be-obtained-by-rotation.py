class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
#         # check if same
#         if mat == target:
#             return True
#         # at most 4 rotations before returning to start 
#         n = len(mat[0])
#         for _ in range(3):
#             for i in range(n//2 + n%2):
#                 for j in range(n//2):
#                     temp = mat[n-j-1][i]
#                     mat[n-j-1][i] = mat[n-i-1][n-j-1]
#                     mat[n-i-1][n-j-1] = mat[j][n-i-1]
#                     mat[j][n-i-1] = mat[i][j]
#                     mat[i][j] = temp
#             if mat == target:
#                 return True
#         return False 

        for _ in range(4):  # Try four rotations (0, 90, 180, 270 degrees)
            if mat == target:
                return True
            # Transpose the matrix and then reverse each row
            mat = [list(row) for row in zip(*mat[::-1])]
        return False
        

