class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
         
        upper_bound = max(piles)

        l = 1
        r = upper_bound
        minimum = 99

        while l < r:
            m = (r+l)//2
            hours = 0

            for i in piles:
                hours += math.ceil(i/m)

            if hours <= h:
                r = m
            else:
                l = m + 1
            

        return l