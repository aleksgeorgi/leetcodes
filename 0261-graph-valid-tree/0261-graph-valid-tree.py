class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adj_list = {i:[] for i in range(n)}
        # convert the edges into an adjacency list
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        # check for cycles 
        visited = set()
        
        # traverse with dfs starting with node 0
        is_valid_tree = dfs(0, -1, adj_list, visited)
        
        # if dfs detects a cycle or not all nodes visted, return false not valid tree
        if not is_valid_tree:
            return False
        
        # check if all nodes have been visted 
        if len(visited) != n:
            return False
        
        return True # no cycles and all nodes visited 
        
def dfs(node, parent, adj_list, visited):
    # mark the current node as visited
    visited.add(node)
    
    # traverse all the neighbors of the current node
    for neighbor in adj_list[node]:
        # if the neighbor is the parent, skip it to avoid revisiting the parent endlesslyct
        if neighbor == parent:
            continue
        
        if neighbor in visited:
            return False # we found a cycle if we already visited this neighbor 
    
        # visit the neighbor recursively and if it returns false, propogate the failure
        is_valid_tree = dfs(neighbor, node, adj_list, visited)
        if is_valid_tree == False:
            return False
        
        # if no cycles were found return true
    return True
        