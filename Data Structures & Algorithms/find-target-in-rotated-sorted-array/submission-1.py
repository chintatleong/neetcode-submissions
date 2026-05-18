class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l < r:
            m = (l + r)//2
            
            if nums[m] > nums[r]:
                l = m + 1
            
            else:
                r = m

        end = len(nums) - 1

        if target > nums[end]:
            flip = l - 1
            start = 0
        
        else: 
            flip = end
            start = l

        while start < flip:
            m = (start + flip)//2

            if nums[m] == target:
                return m

            elif nums[m] > target:
                flip = m - 1

            else:
                start = m + 1

        
        return - 1