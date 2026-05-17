class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1

        while top <= bot: 
            # within this range
            middle = (top + bot)//2

            l , r = 0, COLS - 1
            if (matrix[middle][0] <= target and matrix[middle][-1] >= target):
                while l <= r:
                    m = (l+r)//2
                    
                    if (matrix[middle][m] == target):
                        return True
                    elif (matrix[middle][m] > target):
                        r = m - 1
                    else:
                        l = m + 1

                return False

            elif (matrix[middle][0] > target): # search top half
                bot = middle - 1

            elif (matrix[middle][-1] < target): # search bottom half
                top = middle + 1
    

        return False