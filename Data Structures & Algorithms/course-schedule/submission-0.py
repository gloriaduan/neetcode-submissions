class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for item in prerequisites:
            if item[0] in adj:
                adj[item[0]].append(item[1])
            else:
                adj[item[0]] = [item[1]]
            
            if item[1] not in adj:
                adj[item[1]] = []
        
        visited, path = set(), set()

        def dfs(node, adj, visited, path):
            visited.add(node)
            path.add(node)

            for n in adj[node]:
                if n not in visited:
                    if dfs(n, adj, visited, path):
                        return True
                elif n in path:
                    return True

            path.remove(node)
            return False

        for node in adj:
            if node not in visited:
                if dfs(node, adj, visited, path):
                    return False
        
        return True


    

        