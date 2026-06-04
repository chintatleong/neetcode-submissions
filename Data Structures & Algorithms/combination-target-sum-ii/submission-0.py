class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()

        candidates.sort()

        combo = []
        def dfs(start, total):
            
            if total == target:
                res.add(tuple(combo.copy()))
                return 
            
            if total > target: 
                return 

            for i in range(start, len(candidates)):
                if (total + candidates[i]) > target: 
                    return 

                combo.append(candidates[i])
                dfs(i+1, total + candidates[i])
                combo.pop()

        dfs(0,0)
        ress = []
        for tup in res:
            ress.append(list(tup))

        return ress
                