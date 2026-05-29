class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        
        for stone in stones:
            heapq.heappush(maxheap, -stone)


        while True:
            if len(maxheap) == 1:
                return -maxheap[0]
            
            if not maxheap:
                return 0

            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)

            if x == y:
                continue
            
            elif x > y:
                diff = x - y

                heapq.heappush(maxheap, -diff)


        