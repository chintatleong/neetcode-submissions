class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        store = []
        res = [0] * len(temperatures) 

        for i, temp in enumerate(temperatures):

            while store and (temp > store[-1][1]):
                past_day, past_temp = store.pop()
                days_diff = i - past_day
                res[past_day] = days_diff

            store.append((i, temp))

        return res

