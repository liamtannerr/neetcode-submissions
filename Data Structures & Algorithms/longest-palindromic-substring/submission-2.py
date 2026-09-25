class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        res_len = 0
        res = 0

        for i in range(n):

            j, k = i, i
            while j >= 0 and k < n and s[j] == s[k]:
                j -= 1
                k += 1

            if (k-j-1) > res_len:
                res_len = k-j-1
                res = j + 1
            
            j, k = i, i + 1
            while j >= 0 and k < n and s[j] == s[k]:
                j -= 1
                k += 1

            if (k-j-1) > res_len:
                res_len = k-j-1
                res = j + 1

        return s[res: res_len + res]


            