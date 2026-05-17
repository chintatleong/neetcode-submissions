class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window = {}
        td = {}

        for ch in t:
            td[ch] = 1 + td.get(ch,0)

        have = 0
        need = len(td)  # this already give you 
        res, resL = [-1,-1], float('inf')
        l = 0   # left pointer start at 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)   # adding the character of R pointer to the window

            # check if this character is in td and then, check if we satisfy that character's count
            if c in td and window[c] == td[c]: 
                have += 1       # they have same count so one condition met +1

                while have == need:
                    # update our result
                    if (r - l + 1) < resL:
                        res = [l, r]
                        resL = (r - l + 1)

                    # while have == need, pop the L 
                    # pop from dictionary and also move pointer
                    window[s[l]] -= 1

                    if s[l] in td and window[s[l]] < td[s[l]]:    # check if this popped character makes you desatisfied a character condition
                        have -= 1
                    l = l + 1

        l, r = res  # detuple
        return s[l:r+1] if resL != float('inf') else ""


        



        