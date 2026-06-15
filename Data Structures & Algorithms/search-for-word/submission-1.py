class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def explore(row, col, visited, depth, string):
            string.append(board[row][col])
            visited[row][col] = True

            cur = "".join(string)
            if cur == word:
                return True

            if depth > len(word):
                return False

            if row-1 >= 0 and board[row-1][col] == word[depth]:
                if not (visited[row-1][col]):
                    if explore(row-1, col, visited, depth+1, string.copy()):
                        return True

            if row+1 < len(board) and board[row-1][col] == word[depth]:
                if not (visited[row+1][col]):
                    if explore(row+1, col, visited, depth+1, string.copy()):
                        return True

            if col-1 >= 0 and board[row][col-1] == word[depth]:
                if not (visited[row][col-1]):
                    if explore(row, col-1, visited, depth+1, string.copy()):
                        return True

            if col+1 < len(board[0]) and board[row][col+1] == word[depth]:
                if not (visited[row][col+1]):
                    if explore(row, col+1, visited, depth+1, string.copy()):
                        return True

            visited[row][col] = False
            return False
        
        combo = []
        used = [[False] * len(board[0]) for _ in range(len(board))]
        count = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[count]:
                    used[i][j] = True
                    combo.append(board[i][j])
                    count += 1

                    if i-1>=0 and board[i-1][j] == word[count]:
                        if explore(i-1, j, used.copy(), count+1, combo.copy()):
                            return True

                    if i+1<len(board) and board[i+1][j] == word[count]:
                        if explore(i+1, j, used.copy(), count+1, combo.copy()):
                            return True

                    if j-1>=0 and board[i][j-1] == word[count]:
                        if explore(i, j-1, used.copy(), count+1, combo.copy()):
                            return True
                    
                    if j+1<len(board[0]) and board[i][j+1] == word[count]:
                        if explore(i, j+1, used.copy(), count+1, combo.copy()):
                            return True

                    used[i][j] = False
                    count -= 1  
                    combo.pop()

        return False      

        

                    

                    