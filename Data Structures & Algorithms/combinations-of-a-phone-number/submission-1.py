class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def dfs(i, path):
            if i == len(digits):    # hit end of digits
                res.append(path)
                return

            for ch in phone[digits[i]]:
                dfs(i+1, path+ch)    # i and path are copied, both are not modified but are passed as next state
            
        dfs(0, "")
        return res

        # best way to approach this questio is to draw the tree
        
                          
