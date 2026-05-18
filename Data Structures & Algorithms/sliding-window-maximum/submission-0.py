class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # size of window is k
        # array of int is nums
        
        # slide as usual, if the window size is 3  then we slide, find the max and store in an array

        left = 0
        max_arr = []

        for right in range(len(nums)):

            if (right - left + 1) == k:
                window = nums[left:right+1]
                max_num = max(window)
                max_arr.append(max_num)

                left += 1
        
        return max_arr

                
