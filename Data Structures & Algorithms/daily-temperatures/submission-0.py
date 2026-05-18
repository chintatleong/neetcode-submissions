class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # n + j days until temp[i] < temp[i+j]
        # j would be the number we want

        # condition: A[i] < A[j]
        # cal the difference between the current index with the popped element
        output = [0] * len(temperatures)
        i = 0
        stack = []

        for index, value in enumerate(temperatures):
            if value < stack[-1]:
                stack.append(index)
            else:
                while value > stack[-1]:
                    top = stack.pop()
                    output[top] = index - top
                    
            