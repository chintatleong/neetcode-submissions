class TimeMap:

    def __init__(self):
        # key, value, timestamp 
        # multiple values for the same key, different time stamp
        # retrieve needs key and timestamp

        time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        time_map[("alice", 1)] = time_map.get(("alice", timestamp), "") + value

    def get(self, key: str, timestamp: int) -> str:
        value = time_map.get((key, timestamp))
        
