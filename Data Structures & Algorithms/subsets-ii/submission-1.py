class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        subset = []
        def dfs(cur):
            if cur >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[cur])
            dfs(cur+1)

            subset.pop()

            i = 1
            while cur + i < len(nums) and nums[cur+i] == nums[cur]:
                i += 1
            dfs(cur+i)

        dfs(0)
        return res
