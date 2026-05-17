class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # when you see int you push to stack
        # when you see operand you pop from stack til empty, perform the caluclate then push again, loop continues
        num_stack = []

        for ch in tokens:
            if ch[0] == '-' and len(ch) > 1:
                n = len(ch)
                num = ch[1:n]
                num = int(num)
                num_stack.append(-num)
                continue

            if ch.isdigit():
                num = int(ch)
                num_stack.append(num)

            if not ch.isdigit():
                top_index = len(num_stack) - 1

                if ch == '+':
                    number = num_stack[top_index-1] + num_stack[top_index]
                    num_stack.pop()
                    num_stack.pop()
                    num_stack.append(number)

                elif ch == '-':
                    number = num_stack[top_index-1] - num_stack[top_index]
                    num_stack.pop()
                    num_stack.pop()
                    num_stack.append(number)

                elif ch == '/':
                    number = int(num_stack[top_index-1] / num_stack[top_index])
                    num_stack.pop()
                    num_stack.pop()
                    num_stack.append(number)

                else:
                    number = num_stack[top_index-1] * num_stack[top_index]
                    num_stack.pop()
                    num_stack.pop()
                    num_stack.append(number)  

        return num_stack[-1]      