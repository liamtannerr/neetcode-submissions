def valid_queen(r: int, c: int, board: List[str], n: int)->bool:

    for i in range(n):
        row_char = board[r][i]
        col_char = board[i][c]
        if row_char == "Q" or col_char == "Q":
            return False

        if r - i >= 0 and c + i < n:
            if board[r-i][c+i] == "Q":
                return False
        if r - i >= 0 and c - i >= 0:
            if board[r-i][c-i] == "Q":
                return False
        if r + i < n and c + i < n:
            if board[r+i][c+i] == "Q":
                return False
        if r + i < n and c - i >= 0:
            if board[r+i][c-i] == "Q":
                return False

    return True

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []

        def dfs(r):

            if r >= n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):

                if valid_queen(r,c,board,n):
                    board[r][c] = "Q"
                    dfs(r + 1)
                    board[r][c] = "."


        board = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(".")
            board.append(row)

        dfs(0)

        return res 

        