class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        combo = []

        def dfs():
            if len(combo) == len(nums):
                res.append(combo.copy())
                return 

            for n in nums:
                if n in combo:
                    continue

                combo.append(n)
                dfs()
                combo.pop()

        dfs()
        return res
