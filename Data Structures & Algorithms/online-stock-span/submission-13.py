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

        # bigger value to check all previous prices by popping. 
        # if bigger than will absorb the previous price's span and pop that stack
        # so now the smaller one will be gone
        # but the smaller ones span is with the bigger
        # future bigger ones comes in
        # if the even bigger one is bigger than the big one
        # it will certainly be bigger than the popped stack too
        # so absorbing the big one by the bigger one logically make sense
        # if the future one is not bigger than the big one
        # it cannot span pass the bigger one anyway

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)