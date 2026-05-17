class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # min between two number x index between them (index end - index start) 
        length = len(heights)   
        i = 0
        j = length - 1
        largest = 0
        left = 0
        right = length - 1

        while i < j:
            l = heights[i]
            r = heights[j]
            min_length = min(l, r)

            area = min_length * (j - i)

            if area > largest:
                largest = area
                left = i
                right = j
            
            # just so it moves, either one moves but make the smaller one move first
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return largest
        

        