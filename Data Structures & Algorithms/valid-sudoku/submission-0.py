class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        for row in range(ROWS):
            rowSet = set()
            for col in range(COLS):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rowSet:
                    return False
                rowSet.add(board[row][col])
        
        for col in range(COLS):
            colSet = set()
            for row in range(ROWS):
                if board[row][col] == ".":
                    continue
                if board[row][col] in colSet:
                    return False
                colSet.add(board[row][col])
        
        coords = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]

        for coord in coords:
            quadrantSet = set()
            for row in range(coord[0], coord[0] + 3):
                for col in range(coord[1], coord[1] + 3):
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in quadrantSet:
                        return False
                    quadrantSet.add(board[row][col])
        
        return True

