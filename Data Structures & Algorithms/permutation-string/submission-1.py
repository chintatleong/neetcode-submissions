class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        length = len(s1)
        s1_count = {}
        window_count = {}

        for i in range(0, length):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1

        for right in range(len(s2)):
            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            if (right - left + 1) > length:
                window_count[s2[left]] -= 1
                # if the key has value 0, then drop the key so comparing is possible
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                
                # after dropping the key, then we can shrink and advance the left indice
                left += 1
            
            if s1_count == window_count:
                return True
            


        return False