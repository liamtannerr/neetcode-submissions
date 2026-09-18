class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0":
            return 0
        if n == 1:
            return 1
        
        memo = {n:1}

        def dfs(i):
            if i in memo:
                return memo[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            
            if (i + 1 < n) and (s[i] == "1" or (s[i] == "2" and int(s[i + 1]) < 7)):
                res += dfs(i + 2)
            memo[i] = res
            return res

        return dfs(0)
   
            



            

            