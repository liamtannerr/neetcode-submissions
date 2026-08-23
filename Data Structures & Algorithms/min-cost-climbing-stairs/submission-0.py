class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Assume that cost array is at least length 2

        if len(cost) == 2:
            return min(cost[0], cost[1])

        if len(cost) == 3:
            return min(cost[1], cost[0] + cost[2])

        two_step_idx = len(cost) - 1
        one_step_idx = two_step_idx - 1
        two_step_min = cost[two_step_idx]
        one_step_min = cost[one_step_idx]

        cur_step_idx = one_step_idx - 1

        while cur_step_idx >= 1:
             cur_step_cost = cost[cur_step_idx] + min(two_step_min, one_step_min)
             two_step_min = one_step_min 
             one_step_min = cur_step_cost

             cur_step_idx -= 1
             one_step_idx -= 1
             two_step_idx -= 1

        cur_step_cost = min(cur_step_cost, cost[0] + min(two_step_min, one_step_min))

        return cur_step_cost

