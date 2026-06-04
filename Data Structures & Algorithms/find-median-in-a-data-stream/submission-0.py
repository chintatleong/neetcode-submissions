class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.median = None
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minheap, num)
        copy = self.minheap[:]
        length = len(self.minheap) 

        mid = length // 2
        is_even = True if length % 2 == 0 else False

        # example length is 4
        if length:
            if is_even == True:
                self.median = (copy[mid-1] + copy[mid]) / 2
            else:
                self.median = copy[mid]
        

    def findMedian(self) -> float:
        return self.median
        