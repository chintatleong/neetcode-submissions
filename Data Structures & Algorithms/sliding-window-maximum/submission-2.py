class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # size of window is k
        # array of int is nums
        
        # slide as usual, if the window size is 3  then we slide, find the max and store in an array

        left = 0
        max_arr = []
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            if i >= k - 1:
                while heap[0][1] < (i - k + 1):
                    heap.heappop(heap)
                
                max_arr.append(-heap[0][0])
        
        return max_arr

                
