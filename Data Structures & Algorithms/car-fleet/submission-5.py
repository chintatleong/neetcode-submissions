class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # speed * time = distance
        
        cars = sorted(zip(position, speed))
        times = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            times.append(time)


        fleets = len(set(times))

        return fleets

