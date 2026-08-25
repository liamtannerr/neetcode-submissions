class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n 
        
        dp = [0] * 2
        dp[0], dp[1] = 1, 2
        for i in range(n - 2):
            temp = dp[1]
            dp[1] = dp[0] + temp
            dp[0] = temp
        return dp[1] 