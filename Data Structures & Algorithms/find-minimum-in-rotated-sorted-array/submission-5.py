class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        best = float("inf")

        while True:
            m = (l+r)//2

            if l == r:
                return nums[l]

            elif nums[m] <= nums[r]:
                r = m 

            elif nums[m] > nums[r]:
                l = m + 1
            

            
