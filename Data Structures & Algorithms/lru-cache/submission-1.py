class LRUCache:

    def __init__(self, capacity: int):
        self.LRU = {}
        self.capacity = capacity
        self.time = 0
        

    def get(self, key: int) -> int:
        self.time += 1
        if key in self.LRU:
            self.LRU[key] = (self.LRU[key][0], self.time)
            return self.LRU[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.time += 1
        if key in self.LRU:
            self.LRU[key] = (value, self.time)
        else:
            if (len(self.LRU) < self.capacity):
                self.LRU[key] = (value, self.time)
                
            else:
                oldest = float('inf')
                oldest_key = None
                for k, val in self.LRU.items(): # make sure to use .items() rather than enumerate
                    if (val[1] < oldest):
                        oldest_key = k
                        oldest = val[1]
                
                del self.LRU[oldest_key]

                self.LRU[key] = (value, self.time)


            
