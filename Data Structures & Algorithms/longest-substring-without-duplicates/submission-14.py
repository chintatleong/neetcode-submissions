class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seen = set()
        longest = 0

        while l <= (len(s) - 1) and r <= (len(s) - 1):

            if s[r] not in seen:
                seen.add(s[r])
                longest = max(longest, r - l + 1)

            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1

                seen.add(s[r])

            r = r + 1
        return longest