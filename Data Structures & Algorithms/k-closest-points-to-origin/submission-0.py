class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self,other):
        self_dist = math.sqrt((self.x - 0)**2 + (self.y - 0)**2)
        other_dist = math.sqrt((other.x - 0)**2 + (other.y - 0)**2)

        return self_dist < other_dist

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # smallest (Euclidean distance)

        minheap = []

        for n in points:
            point = Point(n[0],n[1])

            heapq.heappush(minheap,point)

        res = []
        for _ in range(k):
            point = heapq.heappop(minheap)
            res.append([point.x,point.y])
        return res

