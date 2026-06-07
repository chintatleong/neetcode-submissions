class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        s_dict = {}

        for n in t:
            t_dict[n] = t_dict.get(n, 0) + 1

        required = len(t_dict)
        have = 0

        l, r = 0, 0
        best = float("inf")
        output = ""


        while l < len(s) and r < len(s):
            s_dict[s[r]] = s_dict.get(s[r], 0) + 1

            if s[r] in t_dict and s_dict[s[r]] == t_dict[s[r]]:
                have += 1

            while have == required:
                if r - l + 1 < best:
                    best = r - l + 1
                    output = s[l:r + 1]

                if s[l] in t_dict and s_dict[s[l]] == t_dict[s[l]]:
                    have -= 1

                s_dict[s[l]] = s_dict.get(s[l], 0) - 1
                l += 1

            r += 1

        return output


        # s[0,0] = ""
        # s[0,1] = "O"



        