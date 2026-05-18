class MinStack:

    def __init__(self): 
        self.topp = None
        self.count = 0
        self.minimum = 2^32
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.topp = val
        
        if self.minimum > val:
            self.minimum = val

        self.min_stack.append((val, self.minimum))

    def pop(self) -> None:
        self.stack.pop()

        if len(self.stack) > 0:
            self.topp = self.stack[-1]

        self.min_stack.pop()

    def top(self) -> int:
        return self.topp

    def getMin(self) -> int:
        return self.min_stack[-1][1]
        
