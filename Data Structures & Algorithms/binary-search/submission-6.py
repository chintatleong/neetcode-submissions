class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        
        if length == 0:
            return -1

        middle = length // 2
        start = 0
        end = length - 1

        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            # search left half
            end = middle - 1
            return self.binary_search(start, end, nums, target)
        elif nums[middle] < target:
            # search right half
            start = middle + 1
            return self.binary_search(start, end, nums, target)
        else:
            return -1
        
    def binary_search(self, start, end, nums, target):
        if start > end:
            return -1
        
        check = (end - start)//2 + start 

        if nums[check] == target:
            return check
        elif nums[check] > target:
            # search left half
            end = check - 1
            return self.binary_search(start, end, nums, target)
        elif nums[check] < target:
            # search right half
            start = check + 1
            return self.binary_search(start, end, nums, target)
        else:
            return -1


        
        
