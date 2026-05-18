class Solution:
    def findMin(self, nums: List[int]) -> int:
        # either minimum on the R part
        # or minimum on the L part

        # if Right end is smaller than L end, min on R side
        # if R end is bigger than L end, min on L side
        best = float('inf')
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r)//2 

            best = min(best, nums[m])

            if (nums[m] > nums[-1]):
                l = m + 1
            else:
                r = m - 1

        return best
