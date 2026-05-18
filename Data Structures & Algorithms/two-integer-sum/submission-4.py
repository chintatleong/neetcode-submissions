class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = Counter(nums)
        
        for i, num in enumerate(nums):
            difference = target - num

            if difference in table:
                return [i, nums.index(difference)]

        

