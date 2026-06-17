class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode() 
            cur = cur.children[ch]
        cur.endOfWord = True        

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(cur, word):
            if not word:
                return cur.endOfWord
            
            if word[0] == '.':
                if not cur.children:
                    return False
                else:
                    for key in cur.children:
                        if dfs(cur.children[key], word[1:]):
                            return True
                    return False
            
            else:
                if word[0] not in cur.children:
                    return False
                cur = cur.children[word[0]]
                return dfs(cur, word[1:])      

        return dfs(cur,word)





        # cur = self.root

        # for ch in word:
        #     if ch == '.':
        #         if not cur.children:
        #             return False
        #         else:
        #             for key in cur.children:
        #                cur = cur.children[key] 
        #     else:
        #         if ch not in cur.children:
        #             return False 
        #         cur = cur.children[ch]
        
        # if cur.endOfWord == False:  
        #     return False

        # return True 
    
        
