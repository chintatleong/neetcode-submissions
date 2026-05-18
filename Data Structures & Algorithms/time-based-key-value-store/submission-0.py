class TimeMap:

    def __init__(self):
        self.map = dict()
        self.prev_timestamp = 0
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key] = self.map.get(key, [])
        self.map[key].append((timestamp, value))
        self.prev_timestamp = timestamp
        

    def get(self, key: str, timestamp: int) -> str:
        l = 0 
        li = self.map[key] 
        r = len(self.map[key]) - 1
        res = ""

        while l <= r:
            m = (l+r)//2

            if li[m][0] <= timestamp:
                l = m + 1
                res = li[m][1]
            
            else:
                r = m - 1 

        return res