class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
         
        # time = ceil(x/k)

        maxi = max(piles)

        l = 1
        r = maxi

        best_k = 99


        while l <= r:
            k = (l+r)//2
            time = 0

            for x in piles:
                time += math.ceil(x/k)

            
            if (time <= h):
                r = k - 1
                best_k = min(best_k, k)
            else:
                l = k + 1

        return best_k    