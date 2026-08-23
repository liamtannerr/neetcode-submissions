class Solution:

    def formsFleet(self, pos1: int, speed1: int, pos2: int, speed2: int, target: int) -> bool:
        time1 = (target - pos1) / speed1
        time2 = (target - pos2) / speed2
        return time1 <= time2


    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleets = 1
        cars = {}
        for i in range(len(position)):
            cars[position[i]] = speed[i]
        
        position.sort()
        for i in range(len(position) - 1, -1, -1):
            if i <= 0:
                break
            j = i - 1
            if self.formsFleet(position[j], cars[position[j]], position[i], cars[position[i]], target):
                position[j] = position[i]
            else:
                fleets += 1

        return fleets
        