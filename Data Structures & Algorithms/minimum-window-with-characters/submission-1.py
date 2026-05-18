class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        s_dict = {}
        left = 0
        min_str = ""
        min_length = 10000
        t_unique = 0
        s_unique = 0


        # store frequency of characters in t first - Done
        for ch in t:    
            t_dict[ch] = t_dict.get(ch, 0) + 1
        
        for key in t_dict:
            t_unique += 1

        # Sliding windos from left to right 
        for right in range(len(s)):
            placeholder = ""
            if s[right] in t_dict:
                s_dict[s[right]] = s_dict.get(s[right], 0) + 1

            # keep sliding until the frequency of s is equal to t
            while s_dict[s[right]] == t_dict[s[right]]:
                placeholder = s[left:right]
                if s[left] in t_dict:
                    if s_dict[s[left]] == 0:
                        del s_dict[s[left]]
                    s_dict[s[left]] -= 1
                left += 1
            
            p_length = len(placeholder)

            if min(p_length, min_length) == p_length:
                min_str = placeholder
                min_length = p_length

        return min_str       

            # if A:1 B:1 C:1, then we we record this string
            # by doing string = s[left: right]
            # if equal again. do max(string, min)
            # do a while loop to remove element from dict, until dict is not equal
            # then advance right pointer

        