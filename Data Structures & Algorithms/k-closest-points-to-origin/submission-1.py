class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # smallest (Euclidean distance)
        maxheap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            # distance is negated by points stay same
            heapq.heappush(maxheap,[dist, x, y])

        # to build answer
        res = []
        # keep maxheap size k big (answer contianed within)
        while len(maxheap) > k:
            dist, x, y = heapq.heappop(maxheap)
            res.append([x,y])

        return res

