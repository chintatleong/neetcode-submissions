class TimeMap:

    def __init__(self):
        # key, value, timestamp 
        # multiple values for the same key, different time stamp
        # retrieve needs key and timestamp
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key] = self.time_map.get(key, [])
        self.time_map[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            key_list = self.time_map.get(key)
        else:
            return ""
            
        best_time = float('-inf')
        best_value = ""
        l, r = 0, len(key_list) - 1

        while l <= r:
            m = (l+r)//2

            if (key_list[m][1] <= timestamp):
                if (key_list[m][1] > best_time):
                    best_time = key_list[m][1]
                    best_value = key_list[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return best_value