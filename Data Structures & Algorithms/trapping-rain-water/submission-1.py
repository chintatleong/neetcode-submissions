class Solution:
    def trap(self, height: List[int]) -> int:

        length = len(height)
        prefix = [0] * length
        suffix = [0] * length
        l = 0
        r = length - 1

        prefix_max = 0
        for i in range(len(height)):
            if height[i] > prefix_max:
                prefix_max = height[i]
            prefix[i] = prefix_max

        suffix_max = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > suffix_max:
                suffix_max = height[i]
            suffix[i] = suffix_max

        result = [0] * length
        total = 0
        for i in range(len(height)):
            result[i] = min(prefix[i], suffix[i]) - height[i]
            total = total + result[i]
        
        return total

# index_water = min(height[l], height[r]) - height[i]

        