class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        def dfs(row, col, visited, prevHeight):
            if ((row, col) in visited) or (row < 0 or row >= rows or col < 0 or col >= cols) or (heights[row][col] < prevHeight):
                return 

            visited.add((row, col))
            for row_off, col_off in [(1,0), (0,1), (-1,0), (0, -1)]:
                r, c = row + row_off, col + col_off
                dfs(r, c, visited, heights[row][col])

        
        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])

        return res

