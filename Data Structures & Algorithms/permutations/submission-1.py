class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        combo = []
        pick = [False] * len(nums)

        def dfs():
            if len(combo) == len(nums):
                res.append(combo.copy())
                return 

            for i,n in enumerate(nums):
                if pick[i]:
                    continue

                combo.append(n)
                pick[i] = True
                dfs()
                combo.pop()
                pick[i] = False

        dfs()
        return res
