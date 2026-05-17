class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix 
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * suffix
            suffix = nums[i] * suffix

        return output
        