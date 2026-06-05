class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combo = []
        res = []
        open_count = 0
        close_count = 0

        # () valid, (()) valid
        # if (, either ())(

        choices = ["(", ")"]

        def dfs(open_count, close_count):
            # valid
            if open_count == n and close_count == n:
                "".join(combo)
                res.append("".join(combo))
                return

            # invalid
            if close_count > open_count:
                return

            if open_count > n or close_count > n:
                return


            combo.append("(")
            dfs(open_count+1, close_count)
            combo.pop()


            combo.append(")")
            dfs(open_count, close_count+1)
            combo.pop()

            
        dfs(0,0)
        return res
            

