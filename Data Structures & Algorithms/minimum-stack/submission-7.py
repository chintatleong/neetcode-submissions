class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = 99999999999999999999999999999999999
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if (val < self.minimum):
            self.minimum = val
            self.min_stack.append(val)

        

    def pop(self) -> None:
        if not self.stack:
            return

        self.stack.pop()
        self.min_stack.pop()

        if self.min_stack:
            self.minimum = self.min_stack[-1]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum
        
