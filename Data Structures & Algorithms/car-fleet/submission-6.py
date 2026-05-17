class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # speed * time = distance
        
        cars = sorted(zip(position, speed), reverse=True)
        times = []

        for i in range(len(position)):
            time = (target - cars[i][0]) / cars[i][1]

            if times and (time <= times[-1]):
                continue
            else:
                times.append(time)

        fleets = len(times)

        return fleets

