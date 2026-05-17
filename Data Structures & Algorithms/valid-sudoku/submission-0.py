class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            set1 = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in set1:
                        return False
                    set1.add(board[i][j]) 

        for i in range(9):
            set1 = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in set1:
                        return False
                    set1.add(board[j][i])       

        for row in range(9):
            box = set()
            box_in_ho = row % 3
            box_in_ver = row // 3
            for col in range(9):
                i = (col // 3)
                j = (col % 3)
                val = board[i+box_in_ver*3][j+box_in_ho*3]
                if val != ".":
                    if val in box:
                        return False
                    box.add(val)
        
        return True


