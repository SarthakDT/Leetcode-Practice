class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for p, s in zip(position, speed):
            time.append((target - p) / s)
        
        cars = list(zip(position,time))

        cars.sort()

        fleet = 1
        fleet_time = cars[len(cars)-1][1]
        for i in range(len(cars)-2, -1, -1):
            if cars[i][1] > fleet_time:
                fleet+=1
                fleet_time = cars[i][1]
        
        return fleet