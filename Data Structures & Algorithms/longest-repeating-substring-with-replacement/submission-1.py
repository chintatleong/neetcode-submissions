class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        window_size = 0
        
        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 0
            
            freq[s[right]] += 1
            
            # if exist the limit, then, shrink the window with left, until no longer > 2.
            # Then, right should continue to grow
            while ((right - left + 1) - max(freq.values()) > k):
                freq[s[left]] -= 1
                left += 1

            # calculate window and store biggest window
            size = right - left + 1
            window_size = max(window_size, size)

        return window_size
            

        

