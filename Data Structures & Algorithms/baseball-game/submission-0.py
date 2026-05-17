class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ch in operations:

            if ch == "+":
                s = stack[-1] + stack[-2]
                stack.append(s)

            elif ch == "C":
                stack.pop()

            elif ch == "D":
                d = stack[-1] * 2
                stack.append(d)
            
            else:
                stack.append(int(ch))

        total = 0
        for val in stack:
            total += val
    
        return total 

            