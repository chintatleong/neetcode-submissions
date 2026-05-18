class Solution:
    def isValid(self, s: str) -> bool:
        store = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                store.append(ch)

        

        for i in range(len(store)):

            if s[i] == ')':
                top = store.pop()
                if top != '(':
                    return False

            if s[i] == ']':
                top = store.pop()
                if top != '[':
                    return False

            if s[i] == '{':
                top = store.pop()
                if top != '{':
                    return False

        return True