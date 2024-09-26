class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0 
        bottom_edge = 0
        top_edge = len(grid)-1
        left_edge = 0 
        right_edge = len(grid[0])-1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # look at a cell
                if grid[r][c] == 1:
                    
                    # check if we're at a boundary 
                    
                    # row boundary
                    if r == bottom_edge:
                        perimeter += 1
                    else:
                        # check down 
                        if grid[r-1][c] == 0:
                            perimeter += 1 
                            
                    if r == top_edge:
                        perimeter += 1
                    else:
                        # check up
                        if grid[r+1][c] == 0:
                            perimeter += 1
                            
                    # column boundary 
                    if c == left_edge:
                        perimeter += 1
                    else:
                        # check left
                        if grid[r][c-1] == 0:
                            perimeter += 1
                            
                    if c == right_edge:
                        perimeter += 1
                    else:
                        # check right 
                        if grid[r][c+1] == 0:
                            perimeter += 1
                            
                    
        return perimeter