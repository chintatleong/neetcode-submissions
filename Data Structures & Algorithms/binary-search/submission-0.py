class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)

        middle = length//2

        if nums[middle] == target:
            return int(middle)
        
        elif nums[middle] < target:
            return self.helper(nums[length/2:], target)
        
        else:
            return self.helper(nums[:middle], target)

    
    def helper(self, arr, target):
        length = len(arr)

        middle = length // 2

        if middle == 0:
            return -1

        elif arr[middle] == target:
            return int(middle)
        
        elif arr[middle] < target:
            return self.helper(arr[middle:], target)
        
        else:
            return self.helper(arr[:middle], target)

