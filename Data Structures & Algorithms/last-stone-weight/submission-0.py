class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop_max(stones)
            stone_2 = heapq.heappop_max(stones)
            if stone_1 > stone_2:
                heapq.heappush_max(stones, stone_1 - stone_2)
            
        if stones:
            return stones[0]

        return 0