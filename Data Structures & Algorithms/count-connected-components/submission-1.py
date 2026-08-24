class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        visited = set()
        res = 0 

        for item in edges:
            if item[0] not in adj:
                adj[item[0]] = [item[1]]
            elif item[0] in adj:
                adj[item[0]].append(item[1])

            if item[1] not in adj:
                adj[item[1]] = [item[0]]
            elif item[1] in adj:
                adj[item[1]].append(item[0])
        
        def dfs(node, visited):
            visited.add(node)
            
            for n in adj[node]:
                if n not in visited:
                    dfs(n, visited)
        
        for node in adj:
            if node not in visited:
                dfs(node, visited)
                res += 1
        
        res += n - len(visited)

        return res