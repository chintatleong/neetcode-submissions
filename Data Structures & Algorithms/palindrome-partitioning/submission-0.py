class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        combo = []

        def dfs(start):
            # base
            if start >= len(s):
                res.append(combo.copy())
                return

            for end in range(start, len(s)):
                if s[start:end+1] == s[start:end+1][::-1]:
                    combo.append(s[start:end+1])
                    dfs(end+1)
                    combo.pop()


        dfs(0)
        return res

        