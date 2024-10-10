class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        
        # convert the edge list into adj list
        adj_list = [[] for _ in range(n)]
        
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
                
        visited = set()
        
        def dfs(node, parent):
            if node in visited: return;
            
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue # skip to prevent endless loop 
                if neighbor in visited:
                    return False
                result = dfs(neighbor, node)
                if not result: return False
            return True
    
        return dfs(0, -1) and len(visited)==n
                    