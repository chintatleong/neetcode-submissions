class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        combo = []
        def dfs(start, total):
            
            if total == target:
                res.append(combo.copy())
                return 
            
            if total > target: 
                return 

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if (total + candidates[i]) > target: 
                    return 

                combo.append(candidates[i])
                dfs(i+1, total + candidates[i])
                combo.pop()

        dfs(0,0)
        return res
                