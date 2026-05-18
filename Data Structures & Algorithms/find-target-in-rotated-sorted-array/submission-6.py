class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        best = float('inf')
        pivot = 99

        while l <= r:
            m = (l+r)//2 

            if (best > nums[m]):
                best = nums[m]
                pivot = m

            if (nums[m] > nums[-1]):
                l = m + 1
            else:
                r = m - 1


        if target < nums[-1]:
            r = len(nums) - 1
            l = pivot

        elif target > nums[-1]:
            r = pivot - 1
            l = 0 
        
        else:
            return len(nums) - 1

        
        while l <= r:
            m = (l+r) // 2

            if (nums[m] == target):
                return m
            elif (nums[m] < target):
                l = m + 1
            else:
                r = m - 1
        
        return -1
