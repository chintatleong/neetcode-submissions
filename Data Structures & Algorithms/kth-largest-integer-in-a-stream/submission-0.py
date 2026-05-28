class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for val in nums: 
            heapq.heappush(self.heap, -val)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,-val)
        
        temp = self.heap[:]
        res = 0

        for _ in range(self.k):
            res = -heapq.heappop(temp)

        return res
