class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [n* ["."] for _ in range(n)]

        # board nxn "."

        # Checks: if hori, vet and diag have Q, then invalid, return false, place another
        # Base: if queens == n, return True, record the board 
        res = []
        def dfs(queens, row):
            # base case
            if queens == n:
                str_board = []
                for li in board:
                    line = "".join(li)
                    str_board.append(line)

                res.append(str_board.copy())   # need to convert later
                return True


            for j in range(n):
                # invalid check
                if check(n, row, j):
                    board[row][j] = "Q"
                    dfs(queens+1, row+1)
                    board[row][j] = "."

        
        def check(n,row,col):
            for i in range(n):
                if i != row and board[i][col] == 'Q':
                    return False

            
            for j in range(n):
                if j != col and board[row][j] == 'Q':
                    return False

            for i in range(n):
                for j in range(n):
                    if i == row and j == col:   # skip row, col
                        continue
                    
                    if abs(i - row) == abs(j - col) and board[i][j] == "Q":
                        return False

            return True
        
        dfs(0,0)
        return res


            