class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # smallest (Euclidean distance)
        maxheap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            # distance is negated by points stay same
            heapq.heappush(maxheap,[dist, x, y])

            # keep maxheap size k big (answer contianed within), as you push new point if its bigger than k, pop
            if len(maxheap) > k:
                heapq.heappop(maxheap)

        # to build answer
        res = []
        # all the remaining points in maxheap are answers
        while maxheap:
            dist, x, y = heapq.heappop(maxheap)
            res.append([x,y])

        return res

