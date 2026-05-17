class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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

        """
        can swap out the third loop by making another result = [1] * len(nums)
        then in each of the two loops. 
        First does result[i] = prefix
        Second does result[i] = result[i] * postfix
        """

        return output