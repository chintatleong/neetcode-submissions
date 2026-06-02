class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.maxheap = []
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        heapq.heappush(self.maxheap, [-self.time, tweetId, userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        copy = self.maxheap[:]

        followees = set(self.follows.get(userId, []))
        followees.add(userId)

        while copy:
            if len(res) == 10:
                return res

            if copy[0][2] in followees:
                res.append(heapq.heappop(copy)[1])
            else:
                heapq.heappop(copy)
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].discard(followeeId)
        else:
            return


