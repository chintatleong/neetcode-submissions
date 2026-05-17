class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # min between two number x index between them (index end - index start) 
        length = len(heights)   
        i = 0
        j = length - 1
        largest = 0         # track largest area
        left = 0
        right = length - 1

        while i < j:
            l = heights[i]
            r = heights[j]
            min_height = min(l, r)

            area = min_height * (j - i)

            if area > largest:
                largest = area
                left = i
                right = j
            
            # IMPORTANT just so it moves, either one moves but make the smaller one move first
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return largest
        

        