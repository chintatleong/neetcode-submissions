class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        length = len(s1)

        for right in range(len(s2)):
            sorted_sub_s1 = "".join(sorted(s1))
            sorted_sub_s2 = "".join(sorted(s2[right: length + right]))

            if sorted_sub_s1 == sorted_sub_s2:
                return True

        return False