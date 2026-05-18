class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span_list = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, None))
            return 1

        else:
            span = 1
            j = 0

            if self.stack[-1][0] == None:
                self.stack.append((price, span))
                return span

            while price >= self.stack[-1][0]:
                n, past_span = self.stack.pop()
                span = span + past_span
            
            self.stack.append((price, span))

            return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)