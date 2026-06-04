class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        combo = []
        def dfs(i, copy):
        # at each level, all elements can be a choice
        # either take it or take next iteration 
            # base case when you found the target
            if sum(combo) == target:
                res.append(combo.copy())
                return
            
            if sum(combo) > target:
                return

            for index, n in enumerate(copy):
                combo.append(n)
                dfs(index, copy[index:])
                combo.pop()
            return
        
        dfs(0, nums)
        return res
            


