class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span_list = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(price)
            self.span_list.append(None)
            return 1

        else:
            span = 1
            j = 0
            
            if self.stack[-1] == None:
                self.span_list.append(span)
                self.stack.append(price)
                return span

            while price > self.stack[-1-j]:
                span += 1
                j +=1
            
            self.stack.append(price)
            self.span_list.append(span)

            return span

        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)