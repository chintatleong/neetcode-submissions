class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty hash table
        seen = {}

        # loop the list and get the value and index
        for i, num in enumerate(nums):
            diff = target - num

            # check if diff is in the hash table
            if diff in seen:
                return [seen[diff], i]
            # if not in the hash table, put in the hash table
            seen[num] = i
        

