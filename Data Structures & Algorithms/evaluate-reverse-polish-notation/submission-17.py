class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # when you see int you push to stack
        # when you see operand you pop from stack til empty, perform the caluclate then push again, loop continues
        num_stack = []

        for ch in tokens:
            if ch[0] == '-' and len(ch) > 1:        # int() cannot recognise '-11', also this would not be classified as digit too. So need extra guarding
                n = len(ch)             # find length of ch
                num = ch[1:n]           # slice the numeric part
                num = int(num)          # convert to int
                num_stack.append(-num)   # add back that - to the int
                continue

            if ch.isdigit():
                num = int(ch)
                num_stack.append(num)

            if not ch.isdigit():
                if ch == '+':
                    right = num_stack.pop()
                    left = num_stack.pop()
                    number = left + right
                    num_stack.append(number)

                elif ch == '-':
                    right = num_stack.pop()
                    left = num_stack.pop()
                    number = left - right
                    num_stack.append(number)

                elif ch == '/':
                    right = num_stack.pop()
                    left = num_stack.pop()
                    number = int(left / right)                # return floating point val after division but truncate by turn to int
                    num_stack.append(number)

                else:
                    right = num_stack.pop()
                    left = num_stack.pop()
                    number = left * right
                    num_stack.append(number)  

        return num_stack[-1]      