class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first: str
        second:str
        first = "".join(sorted(s))
        second = "".join(sorted(t))

        if (first == second):
            return True

        return False
        