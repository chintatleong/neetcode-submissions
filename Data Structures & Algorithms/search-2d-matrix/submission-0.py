class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_i = 0
        start_j = 0
        end_i = len(matrix) - 1
        end_j = len(matrix[0]) - 1

        while start_i <= end_i or start_j <= end_j:
            middle_i = (end_i - start_i) // 2 + start_i
            




"""
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = (end - start) // 2 + start
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            start = middle + 1
        else:
            end = middle - 1

    return -1

"""