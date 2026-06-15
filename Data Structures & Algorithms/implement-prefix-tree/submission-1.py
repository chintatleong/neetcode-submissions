class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

        """
        Inserting a node would look like this e.g. a
        self.children["a"] = TrieNode()
        """

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        # each ch as TrieNode, access via parent's dict using key
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode() 
            cur = cur.children[ch]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                return False
            else:
                cur = cur.children[ch]
        
        return cur.endOfWord

        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for ch in prefix:
            if ch not in cur.children:
                return False
            else:
                cur = cur.children[ch]
        
        return True
        
        