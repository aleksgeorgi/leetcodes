class Solution:
    def countComponents(self, n, edges):
        components = 0
        visited = [0] * n
        
        # Create an adjacency list
        adjList = [[] for _ in range(n)]
        
        # Populate the adjacency list from the edges
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        # Perform DFS for each unvisited node
        for i in range(n):
            if visited[i] == 0:
                components += 1
                self.dfs(adjList, visited, i)
                
        return components
        
   
    def dfs(self, adjList, visited, startNode):
        visited[startNode] = 1
        
        for neighbor in adjList[startNode]:
            if visited[neighbor] == 0:
                self.dfs(adjList, visited, neighbor)