class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        current = 0
        output = [1] * len(nums)
        left = [1] * len(nums)
        right = [1] * len(nums)
        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            left[i] = prefix
            prefix = nums[i] * prefix
            
        for i in range(len(nums) - 1, -1, -1):
            right[i] = suffix
            suffix = nums[i] * suffix

        for i in range(len(nums)):
            output[i] = left[i] * right[i]

        return output