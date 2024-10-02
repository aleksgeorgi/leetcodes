class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        tri = [[1], [1,1]]
        currRowNum = 1
        
        while len(tri) < numRows:
            # create row with correct number of elemnts:
            nextRow = [0]*(len(tri[currRowNum])+1)
            
            # set left and right pointers of the current row for adding
            currLeft = 0
            currRight = 1
            
            # set the left and right pointers of the next row for receving sums
            nextIndex = 0
            
            while nextIndex < len(nextRow):
                # set the left side = 1
                if nextIndex == 0:
                    nextRow[nextIndex] = 1
                    nextIndex += 1
                # set the right side = 1
                if nextIndex == len(nextRow)-1:
                    nextRow[nextIndex] = 1
                # otherwise take the sum of the above left and the above right and add it 
                else:
                    nextRow[nextIndex] = tri[currRowNum][currLeft] + tri[currRowNum][currRight]
                    currLeft += 1
                    currRight += 1
                nextIndex += 1
                
            # add the summed row to the triangle 
            tri.append(nextRow)
            currRowNum += 1
            
        return tri