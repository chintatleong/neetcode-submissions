class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1

        while top <= bot:
            middle = (bot + top) // 2

            if target > matrix[middle][-1]:
                top = middle + 1
            elif target < matrix[middle][0]:
                bot = middle - 1
            else:
                break 
            
        if not (top <= bot):
            return False
        
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) //2

            if target < matrix[middle][m]:
                r = m - 1
            elif target > matrix[middle][m]:
                l = m + 1
            else:
                return True
        
        return False

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