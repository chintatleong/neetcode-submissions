class Solution:
    def isValid(self, s: str) -> bool:
        store = []

        for i in range(len(store)):
            if ch == '(' or ch == '[' or ch == '{':
                store.append(ch)

            if s[i] == ')':
                top = store.pop()
                if top != '(':
                    return False

            if s[i] == ']':
                top = store.pop()
                if top != '[':
                    return False

            if s[i] == '}':
                top = store.pop()
                if top != '{':
                    return False

        return True