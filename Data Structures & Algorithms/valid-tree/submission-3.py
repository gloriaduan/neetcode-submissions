class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        visited = set()

        for item in edges:
            if item[0] not in adj:
                adj[item[0]] = [item[1]]
            elif item[0] in adj:
                adj[item[0]].append(item[1])
            
            if item[1] not in adj:
                adj[item[1]] = [item[0]]
            elif item[1] in adj:
                adj[item[1]].append(item[0])

        def dfs(node, parent, visited):
            visited.add(node)

            for n in adj[node]:
                if n not in visited:
                    if not dfs(n, node, visited):
                        return False
                elif parent != n:
                    return False

            return True        

        for node in adj:
            if node not in visited:
                if not dfs(node, -1, visited) or len(visited) < n:
                    return False
        
        return True
