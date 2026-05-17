class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set()

        for n in nums:
            num_set.add(n)

        start = set()
        longest = 0

        for n in num_set:
            if (n-1) not in num_set:
                start.add(n)
        
        current = 0
        for n in start:
            length = 1
            i = 1
            while (n + i) in num_set:
                length += 1
                i += 1
            
            if length > longest:
                longest = length
        
        return longest


