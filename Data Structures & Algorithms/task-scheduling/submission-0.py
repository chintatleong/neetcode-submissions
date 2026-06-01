class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1
        
        queue = deque()
        maxHeap = []

        for val in count.values():
            heapq.heappush(maxHeap, -val)

        time = 0

        while maxHeap or queue:
            time += 1

            if not maxHeap:     # case when there is only 1 type of jobs.
                time = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    queue.append([cnt, time + n]) # append the time + cooldown

            if queue and queue[0][1] == time:  # check if cooldown is met, pop if so
                heapq.heappush(maxHeap, queue.popleft()[0])  # just push count
            
        return time

            