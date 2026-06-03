class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i): # pass in index
            if i >= len(nums):  # out of bound
                res.append(subset.copy())
                return
            
            # take i
            subset.append(nums[i])
            dfs(i+1)

            # skip i
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

