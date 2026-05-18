class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car cannot pass another car ahead
        # car can only catch up and go in parallel
        # arg target is the destination
        # when a car catch up to a car fleet at finish is also a fleet
        car_stack = []

        # compact in tuple for sorting
        for i, val in enumerate(position):
            tup = (position[i], speed[i])
            car_stack.append(tup)
        
        # sort in reverse order
        sorted_car_stack = sorted(car_stack, reverse=True)

        # final speed
        final_speed = sorted_car_stack[0][1]

        sorted_time = []
        # time required to get to target for each car
        for i in range(len(sorted_car_stack)):
            time = (target - sorted_car_stack[i][0]) / sorted_car_stack[i][1]
            sorted_time.append(time)
        
        fleet = []

        for i in range(len(sorted_time)):
            if i == 0:  # add lead car
                fleet.append(sorted_time[0])
                continue

            if fleet and sorted_time[i] > fleet[-1]:    # if chase car is slower than add it to the fleet
                fleet.append(sorted_time[i])

            
            

        return len(stack)
