class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        """
        new_s = []
        for c in s:
            if c.isalnum():
                new_s.append(c.lower())

        s = "".join(new_s)
        """

        length = len(s)
        i = 0
        j = length - 1

        while i < length or j > - 1:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True
