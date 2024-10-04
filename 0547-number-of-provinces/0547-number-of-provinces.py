class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        numberOfComponents = 0
        visit = [False] * n

        for i in range(n):
            if not visit[i]:
                numberOfComponents += 1
                self.dfs(i, isConnected, visit) # pass in the data struct to be shared

        return numberOfComponents
    
    def dfs(self, node, isConnected, visit):
        visit[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] == 1 and not visit[i]:
                self.dfs(i, isConnected, visit) # recursive call, pass in same data struct