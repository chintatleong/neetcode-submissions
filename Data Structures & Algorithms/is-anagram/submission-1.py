class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Compare character frequencies using Counter
        return Counter(s) == Counter(t)
        