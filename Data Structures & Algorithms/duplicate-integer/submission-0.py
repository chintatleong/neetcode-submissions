class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for index, num in enumerate(nums):
            for i in range(len(nums)):
                if (i == index):
                    continue
                if (nums[i] == num):
                    return True
        
        return False

# loop, if there is the same int, return true


