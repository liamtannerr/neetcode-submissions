class Solution:

    def canEatAllPiles(self, piles: List[int], h: int, speed: int) -> bool:

        totalTime = 0
        eaten = 0

        for pile in piles:
            totalTime += math.ceil(pile / speed)
            if totalTime > h:
                return False
        
        return totalTime <= h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        maxK = max(piles)
        minK = 1

        while maxK >= minK:
            cur = (maxK + minK) // 2
            if self.canEatAllPiles(piles, h, cur):
                maxK = cur - 1
            else:
                minK = cur + 1

        return minK
        