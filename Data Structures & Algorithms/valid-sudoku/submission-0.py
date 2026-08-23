class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        cols = len(board[0])

        row = [[0 for _ in range(cols)] for _ in range(rows)]
        col = [[0 for _ in range(cols)] for _ in range(rows)]
        square = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            if i < 3:
                curSquare = 0
            elif i < 6:
                curSquare = 3
            else:
                curSquare = 6

            for j in range(cols):
                if j == 3 or j == 6:
                    curSquare += 1
                if board[i][j] == ".":
                    continue
                else:
                    num = int(board[i][j]) - 1
                    if col[j][num] == 1 or row[i][num] == 1 or square[curSquare][num] == 1:
                        return False
                    col[j][num] = 1
                    row[i][num] = 1
                    square[curSquare][num] = 1

        return True


        
        