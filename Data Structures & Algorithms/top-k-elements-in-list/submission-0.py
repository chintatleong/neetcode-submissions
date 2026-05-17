class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)] # nothing appear 0 times so + 1 bucket

        for key, value in freq.items():
            buckets[value].append(key)

        res = []
        for i in range(len(buckets) - 1, 0, -1):    # max indice for the buckets are len(buckets) - 1, length 7 = 0...6
            for num in buckets[i]:
                res.append(num)
                if len(res) ==k:
                    return res


# build an empty list. Loop each bucket and add to list one by one until it reach k.
        
