class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        count = 0
        max_count = 0
        
        for ch in s:
            if ch in seen:
                if max_count < count:
                    max_count = count
                count = 0
            count += 1
            seen.add(ch)

        if max_count < count:
            max_count = count

        return max_count