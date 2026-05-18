class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        window_size = 0
        
        for right in range(len(s)):
            if s[right] not in freq:
                s[right] = 0
            
            s[right] += 1
            



            # calculate window and store biggest window
            size = right - left + 1
            window_size = max(window_size, size)

        return window_size
            

        

