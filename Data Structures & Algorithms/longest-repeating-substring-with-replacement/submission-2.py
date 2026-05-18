class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dup = {}
        l = 0
        r = 0
        len_s = len(s) - 1
        longest = 0

        while l < len_s and r < len_s:

            length = r - l
            longest = max(longest, length)
            
            if dup.get(s[r], 0) >= k:
                while dup.get(s[r]) >= k:
                    dup[s[l]] = dup.get(s[l], 0) - 1
                    l += 1

            dup[s[r]] = dup.get(s[r], 0) + 1
            r += 1
            

        return longest