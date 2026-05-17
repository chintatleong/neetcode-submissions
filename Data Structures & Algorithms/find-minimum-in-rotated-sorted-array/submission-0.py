class Solution:
    def findMin(self, nums: List[int]) -> int:
        # when i > i+1, thats the point
        # if i < i+1 go to the left half
        # if i > i+1 go to right half
        # when it converge, get l 
        # l + 1 will be the minimum 

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r)//2
            
            if nums[m] > nums[r]:
                l = m + 1
            
            else:
                r = m

        return nums[l]