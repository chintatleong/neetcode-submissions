class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums = sorted(nums)

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start = i+1
            end = len(nums) - 1

            while start < end:
                
                if n + nums[start] + nums[end] > 0:
                    end = end - 1
                elif n + nums[start] + nums[end] < 0:
                    start = start + 1
                else: 
                    output.append([n, nums[start], nums[end]])
                    start = start + 1
                    end = end - 1
                    
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
            
        return output