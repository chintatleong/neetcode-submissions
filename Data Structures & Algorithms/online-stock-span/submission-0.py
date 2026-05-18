class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span_list = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.span_list.append(null)
            return 1
        else:
            span = 0
            j = 0
            while price > self.stack[-1-j]:
                span += 1
                j +=1
            
            self.stack.append(price)
            self.span_list(span)

        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)