class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        s2_dict = {}

        for ch in s1:
            s1_dict[ch] = s1_dict.get(ch, 0) + 1

        l = 0
        r = 0

        s2_dict[s2[r]] = s2_dict.get(s2[r], 0) + 1

        while l < len(s2) - 1 and r < len(s2) - 1:

            while r - l + 1 < len(s1):
                r = r + 1
                s2_dict[s2[r]] = s2_dict.get(s2[r], 0) + 1

            if s1_dict == s2_dict:
                return True
        
            r = r + 1

            if r != len(s2) - 1:
               s2_dict[s2[r]] = s2_dict.get(s2[r], 0) + 1


            s2_dict[s2[l]] -= 1
            if s2_dict[s2[l]] == 0:
                del s2_dict[s2[l]]
            l = l + 1
            
            
        return False


