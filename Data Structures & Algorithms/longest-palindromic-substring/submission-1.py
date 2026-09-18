class Solution:
    def longestPalindrome(self, s: str) -> str:
         
        n = len(s)
        memo = [[False] * n for _ in range(n)]
        resIdx = 0
        resLen = 0

        for i in range(n-1, -1, -1):
            for j in range(i, n, 1):
                if (s[i] == s[j]) and (j - i <= 2 or memo[i + 1][j - 1]):
                    memo[i][j] = True
                    if (j - i) > resLen:
                        resIdx = i
                        resLen = j - i

        return s[resIdx : resIdx + resLen + 1]

            