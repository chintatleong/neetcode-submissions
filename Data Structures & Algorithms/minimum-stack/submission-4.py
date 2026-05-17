class MinStack:

    def __init__(self): 
        self.topp = None
        self.count = 0
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.topp = val
        
        if len(self.min_stack) == 0:
            self.min_stack.append((val, val))
        else:
            if self.min_stack[-1][1] > val:
                self.min_stack.append((val, val))
            else:
                self.min_stack.append((val, self.min_stack[-1][1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

        if len(self.stack) > 0:
            self.topp = self.stack[-1]
            self.minimum = self.min_stack[-1][1]


    def top(self) -> int:
        return self.topp

    def getMin(self) -> int:
        return self.min_stack[-1][1]
        
