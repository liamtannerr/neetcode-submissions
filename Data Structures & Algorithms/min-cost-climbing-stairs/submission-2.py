      #
     ## 
    ###
   ####
  #####
 ######
#######


import math

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        costSum = [0] * n
        costSum[0] = 0
        costSum[1] = 0

        for i in range(2, n):
            costSum[i] = min(cost[i - 1] + costSum[i - 1], cost[i - 2] + costSum[i - 2])

        return min(cost[n - 1] + costSum[n - 1], cost[n - 2] + costSum[n - 2])



