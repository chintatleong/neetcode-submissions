class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -99
        min_price = 99

# loop from l to right
        for price in prices:
            
            # only update min if the current is smaller than previous
            if price < min_price:
                min_price = price

            # calculate profit with each iteration with the smallest value before
            profit = price - min_price
                
            # only update if we find a bigger profit
            if profit > max_profit:
                max_profit = profit
        
        if max_profit < 0:
            return 0

        return max_profit
