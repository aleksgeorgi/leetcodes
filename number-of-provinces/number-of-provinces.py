class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        numProv = len(isConnected[0])
        uf = UnionFind(numProv)

        for row in range(len(isConnected[0])):
            for col in range(len(isConnected[row])):
                if isConnected[row][col] == 1 and uf.find(row)!= uf.find(col): # if we are merging them anew
                    numProv -=1 
                    uf.union(row,col)
    
        print(uf.rank)
        return numProv
    
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x]) # path compression
        return self.root[x]
    
    def union(self, x, y):  
        rootX = self.find(x)
        rootY = self.find(y)
        
        is_merged = False
        if rootX == rootY:
            return is_merged # return false 
        
        is_merged = True
        
        if self.root[rootX] > self.root[rootY]:
            self.root[rootY] = rootX
        elif self.root[rootX] < self.root[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootX] = rootY
            self.rank[rootY] += 1
        
        return is_merged
            
        