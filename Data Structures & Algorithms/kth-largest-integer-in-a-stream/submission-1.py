class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums

        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.heap = []

    #     for val in nums: 
    #         heapq.heappush(self.heap, -val)

    # def add(self, val: int) -> int:
    #     heapq.heappush(self.heap,-val)
        
    #     temp = self.heap[:]
    #     res = 0

    #     for _ in range(self.k):
    #         res = -heapq.heappop(temp)

    #     return res
