class Solution:
    def isValid(self, s: str) -> bool:
        store = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                store.append(s[i])

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
        
        if len(store) > 0:
            return False

        return True