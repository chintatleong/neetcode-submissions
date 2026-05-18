class Solution:
    def isValid(self, s: str) -> bool:
        store = []

        for ch in s:
            store.append(ch)

        for i in range(len(store)):
            top = store.pop()

            if s[i] == '(' and top != ')':
                return False

            if s[i] == '[' and top != ']':
                return False

            if s[i] == '{' and top != '}':
                return False

        return True