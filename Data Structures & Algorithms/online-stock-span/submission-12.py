class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span_list = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and price >= self.stack[-1][0]:
            past_span = self.stack.pop()[1]

            span = span + past_span
        
        self.stack.append((price, span))

        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)