class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(row, col):
            visited.add((row, col))

            for r_off, c_off in [(0,1), (1,0), (0,-1), (-1,0)]:
                r, c = row + r_off, col + c_off
                if (0 <= r < rows and 0 <= c < cols) and ((r, c) not in visited) and (grid[r][c] == "1"):
                    dfs(r, c)

        for row in range(rows):
            for col in range(cols): 
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    islands += 1
        
        return islands