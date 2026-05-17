class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []  # (index, height)
        maxArea = 0

        for index, height in enumerate(heights):
            start = index  # how far left can this bar extend?

            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                maxArea = max(maxArea, h * (index - i))
                start = i  # this bar could have started here too!

            stack.append((start, height))

        # Don't forget bars still in stack — they extend to the end
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea