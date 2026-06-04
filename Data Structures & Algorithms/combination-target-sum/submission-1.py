class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        combo = []
        def dfs(start):
        # at each level, all elements can be a choice
        # either take it or take next iteration 
            # base case when you found the target
            if sum(combo) == target:
                res.append(combo.copy())
                return
            
            if sum(combo) > target:
                return

            for i in range(start, len(nums)):
                combo.append(nums[i])
                dfs(i)
                combo.pop()
            return
        
        dfs(0)
        return res
            


