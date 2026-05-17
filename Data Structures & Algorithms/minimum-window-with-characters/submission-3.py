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
        
        t_unique = len(t_dict)

        # Sliding windos from left to right 
        for right in range(len(s)):
            if s[right] in t_dict:
                s_dict[s[right]] = s_dict.get(s[right], 0) + 1

                # check if current window has at least t_dict elements
                if s_dict[s[right]] == t_dict[s[right]]:
                    s_unique += 1

            # shrink window
            while s_unique == t_unique:
                current_window_size = right - left + 1
            
                if current_window_size < min_length:
                    min_length = current_window_size
                    min_str = s[left:right + 1]

                if s[left] in t_dict:            
                    if s_dict[s[left]] == t_dict[s[left]]:
                        s_unique -= 1
                    s_dict[s[left]] -= 1
            
                left += 1
                

        return min_str       

            # if A:1 B:1 C:1, then we we record this string
            # by doing string = s[left: right]
            # if equal again. do max(string, min)
            # do a while loop to remove element from dict, until dict is not equal
            # then advance right pointer

        