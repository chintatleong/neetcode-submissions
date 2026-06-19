class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):    # standard
        cur = self.root 

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endOfWord = True
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # store each string in a trie
        for word in words:
            self.addWord(word)

        # for each row, loop its col, if + direction char is in trie's child, dfs
        ROWS, COLS = len(board), len(board[0])
        path = set()
        res = set()

        def dfs(r, c, i, string, cur):
            if cur.endOfWord == True:
                res.add(string)

            if (min(r,c) < 0 or
                r >= ROWS or c >= COLS or 
                (r,c) in path or
                board[r][c] not in cur.children
                ):
                return False
            
            path.add((r,c))
            ch = board[r][c]
            cur = cur.children[ch]

            dfs(r+1, c, i+1, string+board[r][c], cur) 
            dfs(r-1, c, i+1, string+board[r][c], cur) 
            dfs(r, c-1, i+1, string+board[r][c], cur) 
            dfs(r, c+1, i+1, string+board[r][c], cur)
            path.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, 0, "", self.root)
        
        return list(res)


    


# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         ROWS, COLS = len(board), len(board[0])
#         path = set()

#         def dfs(r, c, i):
#             if i == len(word):
#                 return True

#             if (min(r, c) < 0 or
#                 r >= ROWS or c >= COLS or
#                 word[i] != board[r][c] or
#                 (r, c) in path):
#                 return False
						
# 						# you only reach here if you are valid
# 						# So you path only update if valid
#             path.add((r, c))
#             res = (dfs(r + 1, c, i + 1) or
#                    dfs(r - 1, c, i + 1) or
#                    dfs(r, c + 1, i + 1) or
#                    dfs(r, c - 1, i + 1))
#             path.remove((r, c))
#             return res
				
# 				# Start searching from every cell
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if dfs(r, c, 0):
#                     return True
#         return False